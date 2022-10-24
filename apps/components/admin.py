from django.contrib import admin

from apps.components.models import ComponentColor, ComponentType, Measure, ComponentBlueprint, ComponentInStock, Shop, \
    ComponentPrice, ComponentTypeProperty, PropertyValue


class PropertyValueInline(admin.TabularInline):
    model = PropertyValue
    fields = ("component_blueprint", "property", "value")
    readonly_fields = ("component_blueprint", )
    extra = 1


class ComponentBlueprintAdmin(admin.ModelAdmin):
    inlines = (PropertyValueInline, )


admin.site.register(ComponentColor)
admin.site.register(Measure)
admin.site.register(ComponentType)
admin.site.register(ComponentBlueprint, ComponentBlueprintAdmin)
admin.site.register(ComponentInStock)
admin.site.register(Shop)
admin.site.register(ComponentPrice)
admin.site.register(ComponentTypeProperty)
admin.site.register(PropertyValue)


