# Generated by Django 4.0.1 on 2022-01-09 17:44

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_location_product_alter_inventory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=17, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
