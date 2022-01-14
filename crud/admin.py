from django.contrib import admin

from .models import Location, Product, Inventory

models = [Location, Product, Inventory]

admin.site.register(models)