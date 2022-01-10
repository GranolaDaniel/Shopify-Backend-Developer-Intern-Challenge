import uuid
from django.db import models
from django.core.validators import MinValueValidator

from decimal import Decimal

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    warehouse_name = models.CharField(max_length=200, unique=True, help_text='Name of the warehouse.')

    def __str__(self):
        return self.warehouse_name
    
    class Meta:
        ordering = ['warehouse_name']
        verbose_name = 'location'

class Shelf(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shelf_name = models.CharField(max_length=200, help_text='Name the storage shelf. Should describe where it\'s located in the warehouse.')

    warehouse = models.ForeignKey(Location, on_delete=models.CASCADE, help_text="The warehouse where this shelf is located.")

    def __str__(self):
        return self.shelf_name + ': ' + self.warehouse.warehouse_name
    
    class Meta:
        ordering = ['shelf_name']
        verbose_name = 'shelf'
        verbose_name_plural = 'shelves'

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True, help_text='Name of the product')
    price = models.DecimalField(max_digits=17, decimal_places=2, help_text='Current price of the product.', validators=[MinValueValidator(Decimal('0.01'))]) #Up to 999 trillion 

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'product'

class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.PositiveIntegerField(default=0, help_text='The amount of product available in this inventory.')

    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, help_text='The shelf that this inventory is stored on.')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, help_text='The product contained in the inventory.')


    def __str__(self):
        return self.product.name + ' Inventory'

    class Meta:
        ordering = ['product']
        verbose_name = 'inventory item'