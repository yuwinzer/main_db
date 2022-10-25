from django.db import models
from django.utils import timezone
from apps.customers.models import Customer, Source
from apps.media.models import Media


class OrderStatus(models.Model):
    """a unit of measurement"""
    title = models.CharField(max_length=32, unique=True)
    note = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "order_statuses"
        verbose_name_plural = "order statuses"

    def __str__(self):
        return f'{self.title}'


class Order(models.Model):
    """a unit of measurement"""
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    send_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    note = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "orders"

    def __str__(self):
        if self.status.title == "Send":
            return f"{self.customer} - {self.status} ({self.send_date})"
        else:
            return f"{self.customer} - {self.status}"


class OrderImage(models.Model):
    """a unit of measurement"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    class Meta:
        db_table = "order_images"
