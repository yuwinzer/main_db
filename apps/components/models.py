from django.db import models

from apps.media.models import Media
from apps.warehouses.models import Warehouse


class Unit(models.Model):
    """a unit of measurement"""

    title = models.CharField(max_length=6)

    class Meta:
        db_table = "units"

    def __str__(self):
        return f"{self.title}"


class ComponentType(models.Model):
    """UV resin, glue, fabric - parent types, jackuard, atlas - subtypes of fabric parent type"""

    title = models.CharField(max_length=24)
    parent_type = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "component_types"

    def __str__(self):
        return f"{self.title}"


class ComponentColor(models.Model):
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200, null=True, blank=True)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "component_colors"

    def __str__(self):
        return f"{self.title}"


class ComponentBlueprint(models.Model):
    title = models.CharField(max_length=256)
    type = models.ForeignKey(
        ComponentType, related_name="component_type", on_delete=models.CASCADE, null=True, blank=True
    )
    subtype = models.ForeignKey(
        ComponentType, related_name="component_subtype", on_delete=models.CASCADE, null=True, blank=True
    )
    is_active = models.BooleanField(default=False)
    note = models.CharField(max_length=200, null=True, blank=True)
    color = models.ForeignKey(ComponentColor, on_delete=models.CASCADE, null=True, blank=True)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "component_blueprints"

    def __str__(self):
        return f"{self.title}"


class ComponentTypeProperty(models.Model):
    """Properties for main component types, fabric type - density property, wide"""

    component_blueprint = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    title = models.CharField(max_length=6)

    class Meta:
        db_table = "component_type_properties"
        verbose_name_plural = "component type properties"

    def __str__(self):
        return f"{self.title}"


class ComponentProperty(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    component_type_property = models.ForeignKey(ComponentTypeProperty, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "component_properties"
        verbose_name_plural = "component properties"

    def __str__(self):
        return f"{self.component_type_property} {self.value}"


class ComponentInStock(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "components_in_stock"
        verbose_name_plural = "components in stock"

    def __str__(self):
        return f"{self.component_blueprint} {self.quantity}"


class Shop(models.Model):
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "shops"

    def __str__(self):
        return f"{self.title}"


class ComponentPrice(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()

    class Meta:
        db_table = "component_prices"

    def __str__(self):
        return f"{self.component_blueprint}"


# class FabricType(models.Model):
#     title = models.CharField(max_length=64)
#
#     class Meta:
#         db_table = "fabric_types"
#
#     def __str__(self):
#         return f"{self.title}"
#
#
# class FabricGroup(models.Model):
#     title = models.CharField(max_length=256)
#
#     class Meta:
#         db_table = "fabric_groups"
#
#     def __str__(self):
#         return f"{self.title}"
#
#
# class FabricColor(models.Model):
#     title = models.CharField(max_length=256)
#
#     class Meta:
#         db_table = "fabric_colors"
#
#     def __str__(self):
#         return f"{self.title}"
#
#
# class Fabric(models.Model):
#     color = models.ForeignKey(FabricColor, on_delete=models.CASCADE)
#     group = models.ForeignKey(FabricGroup, on_delete=models.CASCADE)
#     type = models.ManyToManyField(FabricType)
#     density = models.IntegerField(null=True, blank=True)
#     wide = models.IntegerField(null=True, blank=True)
#     price_per_meter = models.DecimalField(max_digits=8, decimal_places=2)
#     price_per_quad_meter = models.DecimalField(max_digits=8, decimal_places=2)
#
#     class Meta:
#         db_table = "fabrics"
#
#     def __str__(self):
#         return f"{self.group} {self.color}"
