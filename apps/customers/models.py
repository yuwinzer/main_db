from django.db import models


class Source(models.Model):
    title = models.CharField(max_length=128, unique=True)
    link = models.CharField(max_length=1024, blank=True)

    class Meta:
        db_table = "sources"

    def __str__(self):
        return f'{self.title}'


class CustomerContact(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    unique_name = models.CharField(max_length=1024, unique=True)

    class Meta:
        db_table = "customer_contacts"
        verbose_name_plural = "customer contacts"

    def __str__(self):
        return f'{self.source} @{self.unique_name}'


class Customer(models.Model):
    name = models.CharField(max_length=128, blank=True)
    customer_contact = models.ManyToManyField(CustomerContact)
    friends = models.ManyToManyField("self", blank=True)

    class Meta:
        db_table = "customers"

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    title = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = "countries"
        verbose_name_plural = "countries"

    def __str__(self):
        return f'{self.title}'


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=256)
    raw_address_line = models.CharField(max_length=512)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region_state = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    address = models.CharField(max_length=512)
    zip_code = models.CharField(max_length=16, blank=True)
    raw_phone_number = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "addresses"
        verbose_name_plural = "addresses"
