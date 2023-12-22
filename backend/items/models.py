from django.db import models


class Item(models.Model):
    CURRENCY = [("USD", "usd"), ("EUR", "eur"), ("GBP", "gbp")]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY, default="usd")

    def __str__(self):
        return self.name
