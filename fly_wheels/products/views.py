from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, Order, CartItem
from django.views.decorators.http import require_POST

# Shop Views
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

# Cart Views 
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
    cart_item, created = CartItem.objects.get_or_create(order=order, product=product)

    if not created:
        cart_item.quantity += 1
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