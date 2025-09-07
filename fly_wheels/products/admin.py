from django.contrib import admin
from .models import Product, Order, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name", "brand", "size", "weight",
        "price", "pack_size", "in_stock",
    )
    list_filter = ("brand", "category", "size", "weight", "in_stock")
    search_fields = ("name", "brand")

    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Basic", {
            "fields": ("name", "image", "category", "brand", "size", "weight")
        }),
        ("Specs", {
            "fields": ("material", "pack_size")
        }),
        ("Pricing & Stock", {
            "fields": ("price", "compare_at_price", "in_stock")
        }),
        ("Shipping", {
            "fields": ("delivery_estimate",)
        }),
        ("Meta", {
            "classes": ("collapse",),
            "fields": ("created_at", "updated_at")
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "email", "is_paid", "created_at", "paid_at")
    list_filter = ("is_paid", "created_at")
    search_fields = ("user__username", "email")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    list_filter = ("order__is_paid",)
    search_fields = ("order__user__username", "product__name")
