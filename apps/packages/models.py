from django.db import models

from apps.customers.models import Customer, Address
from apps.orders.models import Order


class PackageStatus(models.Model):
    """i.e. delivered, returned"""
    status = models.CharField(max_length=200)

    class Meta:
        db_table = "package_statuses"


class TrackNumber(models.Model):
    number = models.CharField(max_length=200)

    class Meta:
        db_table = "track_numbers"


class TrackNumberHistory(models.Model):
    track_number = models.ForeignKey(TrackNumber, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    place = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "track_numbers_history"


class ShippingMethod(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = "shipping_methods"


class ShippingItem(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        db_table = "shipping_items"


class Package(models.Model):
    """a shipping package"""
    status = models.ForeignKey(PackageStatus, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    shipped_at = models.DateTimeField()
    arrived_at = models.DateTimeField(null=True, blank=True)
    order = models.ManyToManyField(Order)
    note = models.CharField(max_length=200, null=True, blank=True)
    track_number = models.ForeignKey(TrackNumber, on_delete=models.CASCADE)
    weight = models.FloatField()
    sizes = models.CharField(max_length=32)
    ship_price = models.DecimalField(max_digits=8, decimal_places=2)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.CASCADE)
    shipping_item = models.ForeignKey(ShippingItem, on_delete=models.CASCADE)

    class Meta:
        db_table = "packages"
