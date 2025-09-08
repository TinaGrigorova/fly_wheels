from django.shortcuts import render
from products.models import Product
from django.shortcuts import redirect
from django.contrib import messages
from django.utils import timezone
from .models import Newsletter


def home(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def newsletter_subscribe(request):
    if request.method != "POST":
        return redirect(request.META.get("HTTP_REFERER", "home"))
    email = request.POST.get("email", "").strip().lower()
    if not email:
        messages.error(request, "Please enter an email address.")
        return redirect(request.META.get("HTTP_REFERER", "home"))
    obj, created = Newsletter.objects.get_or_create(email=email)
    if not created and not obj.is_subscribed:
        obj.is_subscribed = True
        obj.date_unsubscribed = None
        obj.save()
    messages.success(request, "Thanks! You’re subscribed to our newsletter.")
    return redirect(request.META.get("HTTP_REFERER", "home"))

def newsletter_unsubscribe(request):
    if request.method != "POST":
        return redirect("home")
    email = request.POST.get("email", "").strip().lower()
    try:
        obj = Newsletter.objects.get(email=email)
        obj.is_subscribed = False
        obj.date_unsubscribed = timezone.now()
        obj.save()
        messages.success(request, "You’ve been unsubscribed.")
    except Newsletter.DoesNotExist:
        messages.warning(request, "We couldn’t find that email.")
    return redirect("home")
