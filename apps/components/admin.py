from django.contrib import admin

from apps.components.models import ComponentColor, ComponentType, Unit, ComponentBlueprint, ComponentInStock, Shop, \
    ComponentPrice


admin.site.register(ComponentColor)
admin.site.register(Unit)
admin.site.register(ComponentType)
admin.site.register(ComponentBlueprint)
admin.site.register(ComponentInStock)
admin.site.register(Shop)
admin.site.register(ComponentPrice)

