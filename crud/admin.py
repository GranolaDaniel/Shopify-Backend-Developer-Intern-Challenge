from django.contrib import admin

from .models import Location, Shelf, Product, Inventory

models = [Location, Shelf, Product, Inventory]

admin.site.register(models)