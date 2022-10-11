from django.contrib import admin

from apps.customers.models import Customer, Source, CustomerContact, Address, Country


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "country",
        "state_to_city_line",
        "street_to_app_line",
        "receiver_name",
        "payer_name",
        "phone_number_formatted",
    )


admin.site.register(Customer)
admin.site.register(Source)
admin.site.register(CustomerContact)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
