from django.shortcuts import render
from products.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})