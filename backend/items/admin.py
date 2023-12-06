from django.contrib import admin
from .models import Item, Order


class OrderItemsInline(admin.TabularInline):
    model = Order.items.through


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "description",
    )
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsInline,)

    def calculate_total_cost(self, obj):
        return obj.calculate_total_cost()

    readonly_fields = ("payment_status", "items", "calculate_total_cost")


# Создать админ для налогов, купонов (когда голова пройдет)
