from django.core.management import call_command
import sys
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        #   #   #   #   #   #   APPS.ORDERS    #   #   #   #   #   #   #   #   #   #
        sys.stdout = open('apps/orders/fixtures/order_statuses.json', 'w')
        call_command('dumpdata', 'orders.OrderStatus')

        sys.stdout = open('apps/orders/fixtures/orders.json', 'w')
        call_command('dumpdata', 'orders.Order')

        #   #   #   #   #   #   APPS.CUSTOMERS     #   #   #   #   #   #   #   #   #   #
        sys.stdout = open('apps/customers/fixtures/countries.json', 'w')
        call_command('dumpdata', 'customers.Country')

        sys.stdout = open('apps/customers/fixtures/customers.json', 'w')
        call_command('dumpdata', 'customers.Customer')

        sys.stdout = open('apps/customers/fixtures/addresses.json', 'w')
        call_command('dumpdata', 'customers.Address')

        sys.stdout = open('apps/customers/fixtures/customer_contacts.json', 'w')
        call_command('dumpdata', 'customers.CustomerContact')

        sys.stdout = open('apps/customers/fixtures/sources.json', 'w')
        call_command('dumpdata', 'customers.Source')

        #   #   #   #   #   #   APPS.PRODUCTS     #   #   #   #   #   #   #   #   #   #
        sys.stdout = open('apps/products/fixtures/product_styles.json', 'w')
        call_command('dumpdata', 'products.ProductStyle')

        sys.stdout = open('apps/products/fixtures/product_scales.json', 'w')
        call_command('dumpdata', 'products.ProductScale')

        sys.stdout = open('apps/products/fixtures/product_categories.json', 'w')
        call_command('dumpdata', 'products.ProductCategory')

        sys.stdout = open('apps/products/fixtures/product_colors.json', 'w')
        call_command('dumpdata', 'products.ProductColor')

        #   #   #   #   #   #   APPS.WAREHOUSES     #   #   #   #   #   #   #   #   #   #
        sys.stdout = open('apps/warehouses/fixtures/warehouses.json', 'w')
        call_command('dumpdata', 'warehouses.Warehouse')


