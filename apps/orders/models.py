from django.db import models

from apps.customers.models import Customer, Source
from apps.media.models import Media


class OrderStatus(models.Model):
    """a unit of measurement"""
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "order_statuses"


class Order(models.Model):
    """a unit of measurement"""
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    deadline = models.DateField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "orders"


class OrderImage(models.Model):
    """a unit of measurement"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    class Meta:
        db_table = "order_images"
