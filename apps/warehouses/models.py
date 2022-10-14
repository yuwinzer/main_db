from django.db import models

from apps.users.models import User


class Warehouse(models.Model):
    title = models.CharField(max_length=200)
    address_line = models.CharField(max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "warehouses"
