from django.urls import path
from . import views

urlpatterns = [
    path("orders", views.index),
    path("orders/new_order", views.new_order),
]
