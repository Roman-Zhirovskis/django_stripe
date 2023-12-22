from django.db import models

from items.models import Item
from financial_units.models import Discount, Tax


class Order(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    payment_status = models.BooleanField(default=False)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id}"

    def calculate_total_cost(self):
        return sum(item.price for item in self.items.all())
