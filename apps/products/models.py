from django.db import models

from apps.components.models import ComponentBlueprint, Fabric
from apps.customers.models import Customer
from apps.media.models import Media
from apps.orders.models import Order
from apps.warehouses.models import Warehouse


class ProductStyle(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = "product_styles"


class ProductCategory(models.Model):
    title = models.CharField(max_length=64)
    parent_category = models.ForeignKey(to="self", on_delete=models.CASCADE)
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "product_categories"


class ProductSize(models.Model):
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "product_sizes"


class ProductColor(models.Model):
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_colors"


class ProductBlueprint(models.Model):
    title = models.CharField(max_length=256)
    style_id = models.ForeignKey(ProductStyle, on_delete=models.CASCADE)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    size_id = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    new_version_of = models.ForeignKey("self", related_name='new_version_of_design', on_delete=models.CASCADE)
    part_of = models.ForeignKey("self", related_name='part_of_assembly', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    media = models.ManyToManyField(Media)
    component = models.ManyToManyField(ComponentBlueprint)

    class Meta:
        db_table = "product_blueprints"


class ProductStatus(models.Model):
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "product_statuses"


class Product(models.Model):
    product_blueprint = models.ForeignKey(ProductBlueprint, on_delete=models.CASCADE)
    reserved_for = models.ForeignKey("self", on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2)
    sold_price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField()
    sold_date = models.DateField()
    is_gift = models.BooleanField(default=False)
    is_replacement = models.BooleanField(default=False)

    class Meta:
        db_table = "products"


class ProductRefund(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "product_refunds"


class NewDesignRequest(models.Model):
    """a unit of measurement"""
    product_blueprint = models.ForeignKey(ProductBlueprint, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "new_design_requests"
