from django.contrib import admin

from apps.customers.models import Customer, Source, CustomerSource

admin.site.register(Customer)
admin.site.register(Source)
admin.site.register(CustomerSource)
