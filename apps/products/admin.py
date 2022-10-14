from django.contrib import admin

from apps.products.models import ProductRefund, ProductStyle, ProductCategory, ProductScale, ProductColor, \
    ProductBlueprint, ProductStatus, Product, NewDesignRequest

admin.site.register(ProductStyle)
admin.site.register(ProductCategory)
admin.site.register(ProductScale)
admin.site.register(ProductColor)
admin.site.register(ProductBlueprint)
admin.site.register(ProductStatus)
admin.site.register(Product)
admin.site.register(ProductRefund)
admin.site.register(NewDesignRequest)


