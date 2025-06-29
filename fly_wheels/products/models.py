from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Alloy Wheels', 'Alloy Wheels'),
        ('Track Edition', 'Track Edition'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Alloy Wheels')

    def __str__(self):
        return self.name
