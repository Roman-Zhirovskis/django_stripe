from django.contrib import admin
from financial_units.models import Tax, Discount


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ("name", "percent")
    search_fields = ("name",)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("name", "percent")
    search_fields = ("name",)
