from django.db import models


class Customer(models.Model):
    nickname = models.CharField(max_length=128)
    email = models.EmailField(max_length=64)
    friends = models.ManyToManyField("self")

    class Meta:
        db_table = "customers"


class Address(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "addresses"


class Country(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "countries"


class Source(models.Model):
    name = models.CharField(max_length=128)
    link = models.CharField(max_length=1024)

    class Meta:
        db_table = "sources"


class CustomerSource(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    source_id = models.ForeignKey(Source, on_delete=models.CASCADE)
    link = models.CharField(max_length=1024)

    class Meta:
        db_table = "customer_sources"
