# Generated by Django 4.1 on 2022-09-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ElectricityTariff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                "db_table": "electricity_tariffs",
            },
        ),
        migrations.CreateModel(
            name="ProductCostPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("printing_time", models.DecimalField(decimal_places=2, max_digits=8)),
                ("polishing_time", models.DecimalField(decimal_places=2, max_digits=8)),
                ("gluing_time", models.DecimalField(decimal_places=2, max_digits=8)),
                ("painting_time", models.DecimalField(decimal_places=2, max_digits=8)),
                ("sewing_time", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                "db_table": "product_cost_prices",
            },
        ),
        migrations.CreateModel(
            name="SalaryRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
            options={
                "db_table": "salary_rates",
            },
        ),
        migrations.CreateModel(
            name="USDExchangeRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("EUR", models.DecimalField(decimal_places=4, max_digits=16)),
                ("UAH", models.DecimalField(decimal_places=4, max_digits=16)),
                ("RUB", models.DecimalField(decimal_places=4, max_digits=16)),
            ],
            options={
                "db_table": "usd_exchange_rates",
            },
        ),
    ]
