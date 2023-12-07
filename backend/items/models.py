from django.db import models


class Item(models.Model):
    # Добавить выбор валюты в зависимости от страны
    CURRENCY = [("USD", "usd"), ("EUR", "eur"), ("GBP", "gbp")]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY, default="usd")

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percent = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=100)
    percent = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name


# Создать приложение (модуль) orders, где будут все модели (или в payments (еще думаю))
class Order(models.Model):
    items = models.ManyToManyField(Item, blank=True)
    payment_status = models.BooleanField(default=False)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, null=True)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Order {self.id}"

    def calculate_total_cost(self):
        return sum(item.price for item in self.items.all())
