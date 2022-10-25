from django.contrib import admin

from apps.customers.models import Customer, Source, CustomerContact, Address, Country


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "receiver_name",
        "country",
        "region_state",
        "city",
        "zip_code",
        "address",
        "phone_number",
    )


admin.site.register(Customer)
admin.site.register(Source)
admin.site.register(CustomerContact)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
