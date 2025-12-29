from django.contrib import admin
from .models import Product, Order, CartItem
from .models import ProductReview, WishlistItem, ContactRequest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "size", "category", "price", "in_stock")
    list_filter = ("category", "brand", "size", "in_stock")
    search_fields = ("name", "brand")

    fieldsets = (
        ("Basic info", {
            "fields": (
                "name",
                "image",
                "category",
                "brand",
                "size",
                "weight",
                "material",
                "pack_size",          
                "delivery_estimate",  
                "in_stock",
            )
        }),
        ("Pricing", {
            "fields": (
                "price",
                "compare_at_price",
            )
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at", "updated_at")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "email", "is_paid", "created_at", "paid_at")
    list_filter = ("is_paid", "created_at")
    search_fields = ("user__username", "email")
    readonly_fields = ("created_at", "paid_at")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
    list_filter = ("order", "product")
    search_fields = ("order__user__username", "product__name")


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "created_at")
    list_filter = ("rating", "created_at")


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "created_at")


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "handled")
    list_filter = ("handled",)