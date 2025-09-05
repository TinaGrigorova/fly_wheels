from decimal import Decimal as D
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

import stripe
from django.conf import settings

from .models import Product, Order, CartItem

stripe.api_key = settings.STRIPE_SECRET_KEY


# ------------------------------
# Shop Views
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

def filter_by_brand(request, brand):
    products = Product.objects.filter(brand=brand)
    return render(request, "products/category.html", {
        "title": f"{brand} Wheels",
        "products": products,
    })

def filter_by_size(request, size):
    products = Product.objects.filter(size=size)
    return render(request, "products/category.html", {
        "title": f"{size} Wheels",
        "products": products,
    })

def filter_by_weight(request, weight):
    products = Product.objects.filter(weight=weight)
    return render(request, "products/category.html", {
        "title": f"{weight} kg Wheels",
        "products": products,
    })


# ------------------------------
# Cart Views (DB-backed)
# ------------------------------

@login_required
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)

    quantity = int(request.POST.get("quantity", 1))
    item, created = CartItem.objects.get_or_create(order=order, product=product)
    item.quantity = (item.quantity + quantity) if not created else quantity
    item.save()

    messages.success(request, f"Added {product.name} to your cart.")
    redirect_url = request.POST.get("redirect_url") or reverse("view_cart")
    return redirect(redirect_url)

@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    items = order.items.select_related("product") if order else []
    # NOTE: subtotal is a PROPERTY
    total = sum((i.subtotal for i in items), D("0.00"))
    return render(request, "products/cart.html", {
        "order": order,
        "items": items,
        "total": total,
    })

@login_required
@require_POST
def update_cart_item(request, item_id):
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
def remove_cart_item(request, item_id):
    item = get_object_or_404(
        CartItem, id=item_id, order__user=request.user, order__is_paid=False
    )
    item.delete()
    return redirect("view_cart")


# ------------------------------
# Checkout
# ------------------------------

@login_required
@login_required
def create_checkout_session(request):
    base = request.build_absolute_uri("/").rstrip("/")
    success_url = base + reverse("checkout_success") + "?session_id={CHECKOUT_SESSION_ID}"
    cancel_url  = base + reverse("view_cart")

    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if not order or not order.items.exists():
        messages.info(request, "Your cart is empty.")
        return redirect("view_cart")

    line_items = [{
        "price_data": {
            "currency": "gbp",
            "product_data": {"name": i.product.name},
            "unit_amount": int(i.product.price_pence), 
        },
        "quantity": i.quantity,
    } for i in order.items.select_related("product")]

    session = stripe.checkout.Session.create(
        mode="payment",
        line_items=line_items,
        success_url=success_url,
        cancel_url=cancel_url,
        metadata={"order_id": str(order.id)},
    )
    return redirect(session.url, code=303)

@login_required
@require_GET
def checkout_success(request):
    session_id = request.GET.get("session_id")
    if not session_id:
        return redirect("shop")

    order = None
    try:
        s = stripe.checkout.Session.retrieve(session_id)
        order_id = (s.metadata or {}).get("order_id")
    except Exception:
        order_id = None

    if order_id:
        try:
            order = Order.objects.get(id=order_id)
            if not order.is_paid:
                order.is_paid = True
                order.paid_at = timezone.now()
                order.save()
        except Order.DoesNotExist:
            pass
        
    return render(request, "checkout_success.html", {"order": order})

# ------------------------------
# Orders
# ------------------------------

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user, is_paid=True).order_by("-created_at")
    return render(request, "products/order_history.html", {"orders": orders})
