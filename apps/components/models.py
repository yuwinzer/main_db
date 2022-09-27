from django.db import models

from apps.media.models import Media
from apps.warehouses.models import Warehouse


class ComponentColor(models.Model):
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200, null=True, blank=True)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE)

    class Meta:
        db_table = "component_colors"


class Unit(models.Model):
    """a unit of measurement"""
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "units"


class ComponentType(models.Model):
    title = models.CharField(max_length=24)
    note = models.CharField(max_length=200, null=True, blank=True)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE)

    class Meta:
        db_table = "component_types"


class ComponentBlueprint(models.Model):
    title = models.CharField(max_length=256)
    type = models.ForeignKey(ComponentType, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    note = models.CharField(max_length=200, null=True, blank=True)
    color = models.ForeignKey(ComponentColor, on_delete=models.CASCADE, null=True, blank=True)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "component_blueprints"


class ComponentInStock(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "components_in_stock"


class Shop(models.Model):
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "shops"


class ComponentPrice(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    class Meta:
        db_table = "component_prices"


class FabricTypes(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = "fabric_types"


class FabricCategories(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = "fabric_categories"


class Fabric(models.Model):
    title = models.CharField(max_length=256)
    type = models.ForeignKey(FabricTypes, on_delete=models.CASCADE)
    category = models.ForeignKey(FabricCategories, on_delete=models.CASCADE)

    class Meta:
        db_table = "fabrics"
