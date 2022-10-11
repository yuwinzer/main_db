import json
import os

from django.core.management.base import BaseCommand

from apps.customers.models import Source, CustomerContact, Address, Customer
from apps.customers.models import Country
from apps.users.models import User

DEFAULT_USER_PASSWORD = "123"


def load_from_json(path, filename):
    with open(os.path.join(path, filename + ".json"), mode="r", encoding="utf16") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        #   #   #   #   #   #   APPS.USERS    #   #   #   #   #   #   #   #   #   #
        json_users_path = os.path.join("apps", "users", "fixtures")

        users = load_from_json(json_users_path, "users")
        User.objects.all().delete()
        admin_is_here = False
        users_num = 0
        for user in users:
            new_user = User.objects.create_user(
                id=user["pk"],
                username=user["fields"]["username"],
                first_name=user["fields"]["first_name"],
                last_name=user["fields"]["last_name"],
                email=user["fields"]["email"],
                is_superuser=user["fields"]["is_superuser"],
                is_staff=user["fields"]["is_staff"],
                is_active=user["fields"]["is_active"],
                last_login=user["fields"]["last_login"],
                date_joined=user["fields"]["date_joined"],
                birthday=user["fields"]["birthday"],
                note=user["fields"]["note"],
                banned_at=user["fields"]["banned_at"],
            )
            if new_user.is_superuser:
                admin_is_here = True
            new_user.groups.set(user["fields"]["groups"])
            new_user.user_permissions.set(user["fields"]["user_permissions"])
            # new_user.set_password(user['fields']['password'])
            new_user.set_password(DEFAULT_USER_PASSWORD)
            new_user.save()
            users_num += 1
        print(f"Loaded users.models.User: {users_num}")

        if admin_is_here:
            print("Super user created.")

        #   #   #   #   #   #   APPS.CUSTOMERS     #   #   #   #   #   #   #   #   #   #

        json_customers_path = os.path.join("apps", "customers", "fixtures")

        sources = load_from_json(json_customers_path, "sources")
        Source.objects.all().delete()
        source_num = 0
        for source in sources:
            new_source = Source.objects.create(
                id=source["pk"],
                title=source["fields"]["title"],
                link=source["fields"]["link"],
            )
            new_source.save()
            source_num += 1
        print(f"Loaded customers.models.Source: {source_num}")

        customer_contacts = load_from_json(json_customers_path, "customer_contacts")
        CustomerContact.objects.all().delete()
        customer_contacts_num = 0
        for customer_contact in customer_contacts:
            source, created = Source.objects.get_or_create(id=customer_contact["fields"]["source"])
            new_customer_contact = CustomerContact.objects.create(
                id=customer_contact["pk"],
                source=source,
                unique_name=customer_contact["fields"]["unique_name"],
            )
            new_customer_contact.save()
            customer_contacts_num += 1
        print(f"Loaded customers.models.CustomerContact: {customer_contacts_num}")

        customers = load_from_json(json_customers_path, "customers")
        Customer.objects.all().delete()
        customer_num = 0
        for customer in customers:

            new_customer = Customer.objects.create(
                id=customer["pk"],
                name=customer["fields"]["name"],
            )

            customer_contacts = []
            for customer_contact_id in customer["fields"]["customer_contact"]:
                customer_contact, created = CustomerContact.objects.get_or_create(id=customer_contact_id)
                customer_contacts.append(customer_contact)
            new_customer.customer_contact.set(customer_contacts)

            friends_list = []
            for friends_id in customer["fields"]["friends"]:
                friends, created = Customer.objects.get_or_create(id=friends_id)
                friends_list.append(friends)
            new_customer.friends.set(friends_list)

            new_customer.save()
            customer_num += 1
        print(f"Loaded customers.models.Customer: {customer_num}")

        countries = load_from_json(json_customers_path, "countries")
        Country.objects.all().delete()
        country_num = 0
        for country in countries:
            new_country = Country.objects.create(
                id=country["pk"],
                title=country["fields"]["title"],
            )
            new_country.save()
            country_num += 1
        print(f"Loaded customers.models.Country: {country_num}")

        addresses = load_from_json(json_customers_path, "addresses")
        Address.objects.all().delete()
        addresses_num = 0
        for address in addresses:
            customer, created = Customer.objects.get_or_create(id=address["fields"]["customer"])
            country, created = Country.objects.get_or_create(id=address["fields"]["country"])
            new_address = Address.objects.create(
                id=address["pk"],
                customer=customer,
                country=country,
                state_to_city_line=address["fields"]["state_to_city_line"],
                street_to_app_line=address["fields"]["street_to_app_line"],
                receiver_name=address["fields"]["receiver_name"],
                payer_name=address["fields"]["payer_name"],
                phone_number_provided=address["fields"]["phone_number_provided"],
                phone_number_formatted=address["fields"]["phone_number_formatted"],
            )
            new_address.save()
            addresses_num += 1
        print(f"Loaded customers.models.Address: {addresses_num}")
