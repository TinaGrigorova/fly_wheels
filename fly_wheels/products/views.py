from django.shortcuts import render

def shop(request):
    return render(request, 'products/shop.html')  # You'll create this template later
