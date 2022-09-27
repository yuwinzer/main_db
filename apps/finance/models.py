from django.db import models

from apps.products.models import Product


class SalaryRate(models.Model):
    date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "salary_rates"


class ElectricityTariff(models.Model):
    date = models.DateField()
    tariff = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "electricity_tariffs"


class USDExchangeRate(models.Model):
    date = models.DateField()
    EUR = models.DecimalField(max_digits=16, decimal_places=4)
    UAH = models.DecimalField(max_digits=16, decimal_places=4)
    RUB = models.DecimalField(max_digits=16, decimal_places=4)

    class Meta:
        db_table = "usd_exchange_rates"


class ProductCostPrice(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    printing_time = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    polishing_time = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    gluing_time = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    painting_time = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    sewing_time = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = "product_cost_prices"
