from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Product, Order, CartItem


# ------------------------------
# Shop Views
# ------------------------------

def shop(request):
    alloy_wheels = Product.objects.filter(category='Alloy Wheels')
    track_edition = Product.objects.filter(category='track')
    return render(request, 'products/shop.html', {
        'alloy_wheels': alloy_wheels,
        'track_edition': track_edition,
    })

def alloy_wheels(request):
    wheels = Product.objects.filter(category='Alloy Wheels')
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


# ------------------------------
# Cart Views
# ------------------------------

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
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
    total = 0
    if order:
        total = sum(item.subtotal() for item in order.items.all())
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


@require_POST
@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if order:
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

        return redirect('checkout_success')

    messages.warning(request, "No active order to checkout.")
    return redirect('shop')


@login_required
def checkout_success(request):
    return render(request, 'products/checkout_success.html')
