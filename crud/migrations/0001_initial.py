# Generated by Django 4.0.1 on 2022-01-14 20:32

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the location.', max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'location',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the product', max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Current price of the product. Cannot be less than $0.01.', max_digits=17, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
            options={
                'verbose_name': 'product',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stock', models.PositiveIntegerField(default=0, help_text='The amount of product available in this inventory item.')),
                ('location', models.ForeignKey(blank=True, help_text='The location where this inventory is stored.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='crud.location')),
                ('product', models.ForeignKey(help_text='The product contained in the inventory item.', on_delete=django.db.models.deletion.CASCADE, to='crud.product')),
            ],
            options={
                'verbose_name': 'inventory item',
                'ordering': ['product'],
            },
        ),
    ]
