from django.db import models

from apps.components.models import ComponentBlueprint
from apps.customers.models import Customer
from apps.media.models import Media
from apps.orders.models import Order
from apps.warehouses.models import Warehouse


class ProductStyle(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = "product_styles"

    def __str__(self):
        return f"{self.title}"


class ProductCategory(models.Model):
    title = models.CharField(max_length=64)
    parent_category = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "product_categories"
        verbose_name_plural = "product categories"

    def __str__(self):
        return f"{self.title}"


class ProductScale(models.Model):
    title = models.CharField(max_length=64)
    note = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = "product_sizes"

    def __str__(self):
        return f"{self.title}"


class ProductColor(models.Model):
    title = models.CharField(max_length=64)
    note = models.CharField(max_length=200, blank=True)
    media_thumbnail = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "product_colors"

    def __str__(self):
        return f"{self.title}"


class ProductBlueprint(models.Model):
    title = models.CharField(max_length=256)
    style_id = models.ForeignKey(ProductStyle, on_delete=models.CASCADE)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    size_id = models.ForeignKey(ProductScale, on_delete=models.CASCADE)
    new_version_of = models.ForeignKey(
        "self", related_name="new_version_of_design", on_delete=models.CASCADE, null=True, blank=True
    )
    part_of = models.ForeignKey(
        "self", related_name="part_of_assembly", on_delete=models.CASCADE, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    base_color = models.ForeignKey(ProductColor, related_name="base_color", on_delete=models.CASCADE)
    second_color = models.ForeignKey(
        ProductColor, related_name="second_color", null=True, blank=True, on_delete=models.CASCADE
    )
    # fabric = models.ManyToManyField(Fabric, blank=True)
    media = models.ManyToManyField(Media, blank=True)
    component = models.ManyToManyField(ComponentBlueprint, blank=True)

    class Meta:
        db_table = "product_blueprints"

    def __str__(self):
        return f"{self.title}"


class ProductStatus(models.Model):
    title = models.CharField(max_length=64)
    note = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = "product_statuses"
        verbose_name_plural = "product statuses"

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    product_blueprint = models.ForeignKey(ProductBlueprint, on_delete=models.CASCADE)
    reserved_for = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    cost_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    sold_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    publish_date = models.DateField(null=True, blank=True)
    sold_date = models.DateField(null=True, blank=True)
    is_gift = models.BooleanField(default=False)
    is_replacement = models.BooleanField(default=False)

    @property
    def fabrics(self):
        fabrics = []
        for component in self.product_blueprint.component.all():
            if component.type.title == "Fabric":
                fabrics.append(component.title)
        return ",".join(fabrics)
    class Meta:
        db_table = "products"

    def __str__(self):
        return f"{self.product_blueprint} {self.product_blueprint.base_color} {self.product_blueprint.second_color} {self.fabrics}"


class ProductRefund(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = "product_refunds"

    def __str__(self):
        return f"{self.product}"


class NewDesignRequest(models.Model):
    """a unit of measurement"""

    product_blueprint = models.ForeignKey(ProductBlueprint, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "new_design_requests"

    def __str__(self):
        return f"{self.product_blueprint}"
