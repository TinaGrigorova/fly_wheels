from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ("product", "quantity", "price", "line_total")
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "total", "item_count", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "email", "id")
    readonly_fields = ("total", "created_at", "stripe_payment_intent")

    inlines = (OrderItemInline,)
