from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_CHOICES = [
        ("alloy", "Alloy Wheels"),
        ("track", "Track Edition"),
    ]

    BRAND_CHOICES = [
        ("BBS", "BBS"),
        ("OZ Racing", "OZ Racing"),
        ("Enkei", "Enkei"),
        ("Fox", "Fox"),
    ]

    SIZE_CHOICES = [
        ('17"', '17"'),
        ('18"', '18"'),
        ('19"', '19"'),
        ('20"', '20"'),
    ]

    WEIGHT_CHOICES = [
        ("7-10", "7-10 kg"),
        ("10-13", "10-13 kg"),
        ("13-17", "13-17 kg"),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    compare_at_price = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True,
        help_text="Optional higher price to show a discount."
    )
    image = models.ImageField(upload_to="product_images/")

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="alloy")
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default="BBS")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='18"')
    weight = models.CharField(max_length=10, choices=WEIGHT_CHOICES, default="7-10")

    in_stock = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    @property
    def price_pence(self) -> int:
        """Handy for Stripe (integer minor units)."""
        return int(self.price * Decimal("100"))

    @property
    def on_sale(self) -> bool:
        return bool(self.compare_at_price and self.compare_at_price > self.price)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Order #{self.pk} by {self.user.username}"

    @property
    def total(self) -> Decimal:
        total = Decimal("0.00")
        for item in self.items.select_related("product"):
            total += item.subtotal
        return total

    @property
    def item_count(self) -> int:
        return sum(i.quantity for i in self.items.all())


class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("order", "product")  

    def __str__(self) -> str:
        return f"{self.quantity} × {self.product.name}"

    @property
    def subtotal(self) -> Decimal:
        return (self.product.price or Decimal("0.00")) * self.quantity
