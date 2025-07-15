from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Order, CartItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

def view_cart(request):
    order = get_object_or_404(Order, user=request.user, is_ordered=False)
    total = sum(item.subtotal for item in order.items.all())
    return render(request, 'products/cart.html', {
        'order': order,
        'total': total,
    })

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
    cart_item, created = CartItem.objects.get_or_create(order=order, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')

@login_required
def view_cart(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    return render(request, 'products/cart.html', {'order': order})


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

