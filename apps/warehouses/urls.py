from django.urls import path
from . import views

urlpatterns = [path("warehouses", views.index)]
