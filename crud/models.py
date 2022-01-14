import uuid
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.deletion import SET_NULL

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, help_text='Name of the location.')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'location'

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, help_text='Name of the product')
    price = models.DecimalField(max_digits=17, decimal_places=2, help_text='Current price of the product. Cannot be less than $0.01.', validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'product'

class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.PositiveIntegerField(default=0, help_text='The amount of product available in this inventory item.')

    location = models.ForeignKey(Location, blank=True, null=True, on_delete=SET_NULL, help_text='The location where this inventory is stored.')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='The product contained in the inventory item.')

    def __str__(self):
        return self.product.name + ' Inventory'

    class Meta:
        ordering = ['product']
        verbose_name = 'inventory item'