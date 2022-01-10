from django.contrib import admin

from .models import Location, Shelf, Product, Inventory

models = [Location, Shelf, Product, Inventory]
# Register your models here.
admin.site.register(models)