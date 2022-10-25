from django.contrib import admin

from apps.products.models import ProductRefund, ProductStyle, ProductCategory, ProductScale, ProductColor, \
    ProductBlueprint, ProductStatus, Product, NewDesignRequest, ProductCraft


class ProductCraftAdmin(admin.ModelAdmin):
    list_display = (
        "product_blueprint",
        "component",
        "quantity",
        "main_measure",
    )


class ProductCraftInline(admin.TabularInline):
    model = ProductCraft
    fields = ("component", "quantity")
    readonly_fields = ("product_blueprint", )
    extra = 5


class ProductBlueprintAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "size",
        "base_color",
    )
    inlines = (ProductCraftInline, )


admin.site.register(ProductStyle)
admin.site.register(ProductCategory)
admin.site.register(ProductScale)
admin.site.register(ProductColor)
admin.site.register(ProductBlueprint, ProductBlueprintAdmin)
admin.site.register(ProductCraft, ProductCraftAdmin)
admin.site.register(ProductStatus)
admin.site.register(Product)
admin.site.register(ProductRefund)
admin.site.register(NewDesignRequest)


