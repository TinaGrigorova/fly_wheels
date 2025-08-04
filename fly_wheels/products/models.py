from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('alloy', 'Alloy Wheels'),
        ('track', 'Track Edition'),
    ]

    BRAND_CHOICES = [
        ('BBS', 'BBS'),
        ('OZ Racing', 'OZ Racing'),
        ('Enkei', 'Enkei'),
        ('Fox', 'Fox'),
    ]

    SIZE_CHOICES = [
        ('17"', '17"'),
        ('18"', '18"'),
        ('19"', '19"'),
        ('20"', '20"'),
    ]

    WEIGHT_CHOICES = [
    ('7-10', '7-10 kg'),
    ('10-13', '10-13 kg'),
    ('13-17', '13-17 kg'),
]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Alloy Wheels')
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default='BBS')
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='18"')
    weight = models.CharField(max_length=10, choices=WEIGHT_CHOICES, default='7-10')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.pk} by {self.user.username}"


class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"