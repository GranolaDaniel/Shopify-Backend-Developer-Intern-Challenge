from django.forms import ModelForm

from .models import Location, Shelf, Product, Inventory

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['warehouse_name']

class ShelfForm(ModelForm):
    class Meta:
        model = Shelf
        fields = ['shelf_name', 'warehouse']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['stock', 'shelf', 'product']


