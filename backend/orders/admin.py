from django.contrib import admin

from orders.models import Order


class OrderItemsInline(admin.TabularInline):
    model = Order.items.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsInline,)

    readonly_fields = (
        "payment_status",
        "items",
    )
