from django.forms import ModelForm

from .models import Location, Product, Inventory

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['stock', 'location', 'product']


