from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from store.cart import Cart
from decimal import Decimal

stripe.api_key = settings.STRIPE_SECRET_KEY

from .models import Product, Order, CartItem


# ------------------------------
# Shop Views
# ------------------------------

def shop(request):
    alloy_wheels = Product.objects.filter(category='alloy')
    track_edition = Product.objects.filter(category='track')
    return render(request, 'products/shop.html', {
        'alloy_wheels': alloy_wheels,
        'track_edition': track_edition,
    })

def alloy_wheels(request):
    wheels = Product.objects.filter(category='alloy')
    return render(request, 'products/category.html', {
        'title': 'Alloy Wheels',
        'products': wheels,
    })

def track_edition(request):
    wheels = Product.objects.filter(category='track')
    return render(request, 'products/category.html', {
        'title': 'Track Edition',
        'products': wheels,
    })

def filter_by_brand(request, brand):
    products = Product.objects.filter(brand=brand)
    return render(request, 'products/category.html', {
        'title': f'{brand} Wheels',
        'products': products
    })

def filter_by_size(request, size):
    products = Product.objects.filter(size=size)
    return render(request, 'products/category.html', {
        'title': f'{size}" Wheels',
        'products': products
    })

def filter_by_weight(request, weight):
    products = Product.objects.filter(weight=weight)
    return render(request, 'products/category.html', {
        'title': f'{weight}kg Wheels',
        'products': products
    })



# ------------------------------
# Cart Views
# ------------------------------

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)
    quantity = int(request.POST.get('quantity', 1))

    cart_item, created = CartItem.objects.get_or_create(order=order, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    messages.success(request, f"Added {product.name} to your cart!")
    return redirect('view_cart')


@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    total = sum(item.subtotal() for item in order.items.all()) if order else 0
    return render(request, 'products/cart.html', {'order': order, 'total': total})


@require_POST
@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, order__user=request.user, order__is_paid=False)
    quantity = int(request.POST.get('quantity', 1))

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('view_cart')


@require_POST
@login_required
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, order__user=request.user, order__is_paid=False)
    cart_item.delete()
    return redirect('view_cart')


@login_required
def checkout_success(request):
    session_id = request.GET.get('session_id')
    if not session_id:
        return redirect('shop')

    session = stripe.checkout.Session.retrieve(session_id)
    order_id = session.metadata.get('order_id')

    order = get_object_or_404(Order, id=order_id, user=request.user, is_paid=False)

    # Mark as paid
    order.is_paid = True
    order.save()

    # Send confirmation email
    subject = "Fly Wheels – Order Confirmation"
    html_message = render_to_string('products/email/order_confirmation.html', {
        'user': request.user,
        'order': order,
        'total': sum(item.subtotal() for item in order.items.all()),
    })
    plain_message = strip_tags(html_message)
    recipient = request.user.email
    send_mail(subject, plain_message, None, [recipient], html_message=html_message)

    return render(request, 'checkout_success.html')

    # Clear cart
    cart = Cart(request)
    cart.clear()

    return render(request, 'products/checkout_success.html')


@csrf_exempt
@login_required
def create_checkout_session(request):
    domain = "https://refactored-engine-q79vqwr96v5pf6xrg-8000.app.github.dev"
    order = Order.objects.filter(user=request.user, is_paid=False).first()

    if not order:
        return redirect('view_cart')

    total_amount = int(sum(item.subtotal() for item in order.items.all()) * 100)  # pennies

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': 'Fly Wheels Order',
                },
                'unit_amount': total_amount,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f"{domain}/shop/checkout/success/?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{domain}/shop/cart/",
        metadata={
            'order_id': order.id
        }
    )
    return redirect(session.url, code=303)


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user, is_paid=True).order_by('-created_at')
    return render(request, 'products/order_history.html', {'orders': orders})

def view_cart(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    items = order.items.select_related("product") if order else []
    total = sum((i.subtotal for i in items), Decimal("0.00"))

  
    return render(request, "products/cart.html", {
        "order": order,
        "items": items,
        "total": total,
    })