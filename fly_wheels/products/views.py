from django.shortcuts import render
from .models import Product

def shop(request):
    alloy_wheels = Product.objects.filter(category='Alloy Wheels')
    track_edition = Product.objects.filter(category='track')
    return render(request, 'products/shop.html', {
        'alloy_wheels': alloy_wheels,
        'track_edition': track_edition,
    })