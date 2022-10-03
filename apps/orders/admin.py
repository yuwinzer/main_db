from django.contrib import admin

from apps.orders.models import Order, OrderStatus

admin.site.register(Order)
admin.site.register(OrderStatus)
