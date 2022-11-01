from django.db import models

from apps.media.models import Media
from apps.warehouses.models import Warehouse


class Measure(models.Model):
    """a unit of measurement - l, ml, pc, m"""
    title = models.CharField(max_length=4)
    note = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = "component_measures"

    def __str__(self):
        return f"{self.title}"


class ComponentProperty(models.Model):
    """Properties for components - density, wide, length"""
    title = models.CharField(max_length=64)
    measure = models.ForeignKey(Measure, on_delete=models.CASCADE)

    class Meta:
        db_table = "component_type_properties"
        verbose_name_plural = "component type properties"

    def __str__(self):
        return f"{self.title} {self.measure}"


class ComponentType(models.Model):
    """bolt, paper"""
    title = models.CharField(max_length=24)
    main_property = models.ForeignKey(ComponentProperty, related_name="main_property", on_delete=models.CASCADE)
    properties = models.ManyToManyField(ComponentProperty, blank=True)

    class Meta:
        db_table = "component_types"

    def __str__(self):
        return f"{self.title}"


class ComponentColor(models.Model):
    title = models.CharField(max_length=6)

    class Meta:
        db_table = "component_colors"

    def __str__(self):
        return f"{self.title}"


class ComponentManufacturer(models.Model):
    title = models.CharField(max_length=32)
    link = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "component_manufacturers"

    def __str__(self):
        return f"{self.title}"


class ComponentBlueprint(models.Model):
    title = models.CharField(max_length=256)
    type = models.ForeignKey(
        ComponentType, related_name="component_type", on_delete=models.CASCADE, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    manufacturer = models.ForeignKey(ComponentManufacturer, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(ComponentColor, on_delete=models.CASCADE, null=True, blank=True)
    color_media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "component_blueprints"

    def __str__(self):
        return f"{self.title}"


class ComponentThumbnail(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "component_thumbnails"

    def __str__(self):
        return f"{self.component_blueprint}"


class PropertyValue(models.Model):
    component_blueprint = models.ForeignKey(ComponentBlueprint, on_delete=models.CASCADE)
    property = models.ForeignKey(ComponentProperty, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "component_property_values"
        verbose_name_plural = "component property values"

    def __str__(self):
        return f"{self.component_blueprint} - {self.property} - {self.value}"


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
        db_table = "component_shops"

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
