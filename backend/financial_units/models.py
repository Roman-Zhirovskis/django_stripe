from django.db import models


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


# Create your models here.
