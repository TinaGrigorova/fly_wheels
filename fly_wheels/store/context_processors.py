from products.models import Order

def cart_item_count(request):
    count = 0
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user, is_paid=False).first()
        if order:
            count = sum(item.quantity for item in order.items.all())
    return {'cart_item_count': count}