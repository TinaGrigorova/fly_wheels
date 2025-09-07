from decimal import Decimal as D

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_GET, require_POST
from accounts.utils.mailchimp import subscribe as mc_subscribe
from core.emailing import send_contact_email
import stripe

from .models import Product, Order, CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY


# ------------------------------
# Shop & Filters
# ------------------------------

def shop(request):
    alloy_wheels = Product.objects.filter(category="alloy")
    track_edition = Product.objects.filter(category="track")
    return render(request, "products/shop.html", {
        "alloy_wheels": alloy_wheels,
        "track_edition": track_edition,
    })


def alloy_wheels(request):
    wheels = Product.objects.filter(category="alloy")
    return render(request, "products/category.html", {
        "title": "Alloy Wheels",
        "products": wheels,
    })


def track_edition(request):
    wheels = Product.objects.filter(category="track")
    return render(request, "products/category.html", {
        "title": "Track Edition",
        "products": wheels,
    })


def filter_by_brand(request, brand: str):
    products = Product.objects.filter(brand=brand)
    return render(request, "products/category.html", {
        "title": f"{brand} Wheels",
        "products": products,
    })


def filter_by_size(request, size: str):
    products = Product.objects.filter(size=size)
    return render(request, "products/category.html", {
        "title": f'{size} Wheels',
        "products": products,
    })


def filter_by_weight(request, weight: str):
    products = Product.objects.filter(weight=weight)
    return render(request, "products/category.html", {
        "title": f"{weight} kg Wheels",
        "products": products,
    })


# ------------------------------
# Cart (DB-backed)
# ------------------------------

@login_required
@require_POST
def add_to_cart(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)

    quantity = max(1, int(request.POST.get("quantity", 1)))
    item, created = CartItem.objects.get_or_create(order=order, product=product)
    item.quantity = quantity if created else item.quantity + quantity
    item.save()

    messages.success(request, f"Added {product.name} to your cart.")

    redirect_url = request.POST.get("redirect_url")
    if redirect_url and url_has_allowed_host_and_scheme(redirect_url, {request.get_host()}):
        return redirect(redirect_url)
    return redirect("view_cart")


@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    items = order.items.select_related("product") if order else []
    total = sum((i.subtotal for i in items), D("0.00"))
    return render(request, "products/cart.html", {
        "order": order,
        "items": items,
        "total": total,
    })


@login_required
@require_POST
def update_cart_item(request, item_id: int):
    item = get_object_or_404(
        CartItem, id=item_id, order__user=request.user, order__is_paid=False
    )
    qty = int(request.POST.get("quantity", 1))
    if qty > 0:
        item.quantity = qty
        item.save()
    else:
        item.delete()
    return redirect("view_cart")


@login_required
@require_POST
def remove_cart_item(request, item_id: int):
    item = get_object_or_404(
        CartItem, id=item_id, order__user=request.user, order__is_paid=False
    )
    item.delete()
    return redirect("view_cart")


# ------------------------------
# Checkout (Stripe)
# ------------------------------

def _order_total_cents(order: Order) -> int:
    """Return the order total in integer minor units (pence)."""
    total = D("0.00")
    for i in order.items.select_related("product"):
        total += i.subtotal
    return int((total * 100).quantize(D("1")))


@login_required
@require_POST
def create_checkout_session(request):
    """Create a Stripe Checkout Session and redirect the user there."""
    order = Order.objects.filter(user=request.user, is_paid=False)\
                         .prefetch_related("items__product").first()
    if not order or order.items.count() == 0:
        messages.error(request, "Your cart is empty.")
        return redirect("view_cart")

    line_items = [{
        "quantity": i.quantity,
        "price_data": {
            "currency": "gbp",                               
            "unit_amount": int(i.product.price * 100),      
            "product_data": {"name": i.product.name},
        },
    } for i in order.items.all()]

    success_url = request.build_absolute_uri(reverse("checkout_success")) + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url = request.build_absolute_uri(reverse("view_cart"))

    opt_in = "1" if request.POST.get("opt_in") else "0"

    params = {
        "mode": "payment",
        "line_items": line_items,
        "success_url": success_url,
        "cancel_url": cancel_url,
        "metadata": {
            "order_id": str(order.id),
            "opt_in": opt_in,             
        },
    }
    # Prefill the email field in Stripe Checkout
    if request.user.email:
        params["customer_email"] = request.user.email

    session = stripe.checkout.Session.create(**params)
    return redirect(session.url, code=303)


@login_required
@require_GET
def checkout_success(request):
    """
    Verify the Stripe session, ensure it's paid and amount matches,
    mark the order as paid, optionally subscribe the buyer to marketing,
    send confirmation email, then show the page.
    """
    session_id = request.GET.get("session_id")
    if not session_id:
        return redirect("shop")

    # Retrieve & validate session
    try:
        s = stripe.checkout.Session.retrieve(session_id)
    except Exception:
        messages.error(request, "We couldn't verify your payment session.")
        return redirect("view_cart")

    if getattr(s, "payment_status", None) != "paid":
        messages.warning(request, "Payment not completed yet.")
        return redirect("view_cart")

    order_id = (getattr(s, "metadata", {}) or {}).get("order_id")
    order = None
    if order_id:
        order = (
            Order.objects.filter(id=order_id, user=request.user, is_paid=False)
            .select_related("user")
            .first()
        )

    if not order:
        return render(request, "checkout_success.html", {"order": None})

    # Amount check
    expected_cents = _order_total_cents(order)
    paid_cents = getattr(s, "amount_total", None)
    if paid_cents is not None and int(paid_cents) != expected_cents:
        messages.error(request, "Paid amount didn’t match order total. Please contact support.")
        return redirect("view_cart")

    # Pull email + marketing choice from Stripe up front
    buyer_email = (getattr(s, "customer_details", {}) or {}).get("email") \
                  or getattr(s, "customer_email", None)
    opt_in = (getattr(s, "metadata", {}) or {}).get("opt_in")  # "1" if ticked

    # Mark as paid and store buyer email 
    if not order.is_paid:
        order.is_paid = True
        order.paid_at = timezone.now()
        if buyer_email and hasattr(order, "email"):
            try:
                order.email = buyer_email
            except Exception:
                pass
        order.save()

        # Send confirmation
        recipient = buyer_email or (order.user.email if order.user and order.user.email else None)
        if recipient:
            subject = "Fly Wheels – Order Confirmation"
            html = render_to_string(
                "products/email/order_confirmation.html",
                {"user": order.user, "order": order},
            )
            send_mail(
                subject,
                strip_tags(html),
                settings.DEFAULT_FROM_EMAIL,
                [recipient],
                html_message=html,
                fail_silently=False,
            )

    # Subscribe to Mailchimp if the buyer opted in
    try:
        if opt_in == "1" and buyer_email:
            mc_subscribe(
                buyer_email,
                first_name=(order.user.username if order and order.user else ""),
                tags=["Customer"],
                double_opt_in=True, 
            )
    except Exception:
        pass

    return render(request, "checkout_success.html", {"order": order})


# ------------------------------
# Orders
# ------------------------------

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user, is_paid=True).order_by("-created_at")
    return render(request, "products/order_history.html", {"orders": orders})

# ------------------------------
# Emails 
# ------------------------------


@require_POST
def contact_submit(request):
    name = request.POST.get("name","").strip()
    email = request.POST.get("email","").strip()
    msg = request.POST.get("message","").strip()

    if not (name and email and msg):
        messages.error(request, "Please fill in all fields.")
        return redirect(request.META.get("HTTP_REFERER", "home"))

    send_contact_email(name, email, msg)
    messages.success(request, "Thanks! Your message has been sent.")
    return redirect(request.META.get("HTTP_REFERER", "home"))