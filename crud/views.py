from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Inventory, Location, Product, Shelf
from .forms import LocationForm, ShelfForm, ProductForm, InventoryForm

def index(request):
    context = {}

    return render(request, 'crud/index.html', context)

def add(request, item):
    item = item.lower()

    if item == 'products':
        form = ProductForm
    elif item == 'locations':
        form = LocationForm
    elif item == 'shelves':
        form = ShelfForm
    elif item == 'inventory':
        form = InventoryForm

    if request.method == 'POST':
        form = form(request.POST)

        if form.is_valid():
            #Price validation is being handled by MinValueValidator on the Product model
            form.save()

            return HttpResponseRedirect(reverse('crud:{}'.format(item)))
    else:
        form = form()
    return render(request, 'crud/add_form.html', {'form': form, 'type': item})

def edit(request, item, id):
    item = item.lower()

    if item == 'products':
        form = ProductForm
        edit_item = Product.objects.filter(id=id).first()
    elif item == 'locations':
        form = LocationForm
        edit_item = Location.objects.filter(id=id).first()
    elif item == 'shelves':
        form = ShelfForm
        edit_item = Shelf.objects.filter(id=id).first()
    elif item == 'inventory':
        form = InventoryForm
        edit_item = Inventory.objects.filter(id=id).first()

    if request.method == 'POST':
        form = form(request.POST, instance=edit_item)

        if form.is_valid():
            #Price validation is being handled by MinValueValidator on the Product model
            form.save()

            return HttpResponseRedirect(reverse('crud:{}'.format(item)))
    else:
        form = form(instance=edit_item)

        context = {'edit_item': edit_item, 'form': form, 'type': item}
        
    return render(request, 'crud/edit_form.html', context)

def delete(request, item, id):
    item = item.lower()

    if item == 'products':
        form = ProductForm
        del_item = Product.objects.filter(id=id).first()
    elif item == 'locations':
        form = LocationForm
        del_item = Location.objects.filter(id=id).first()
    elif item == 'shelves':
        form = ShelfForm
        del_item = Shelf.objects.filter(id=id).first()
    elif item == 'inventory':
        form = InventoryForm
        del_item = Inventory.objects.filter(id=id).first()

    if request.method == 'POST':
        del_item.delete()
        return HttpResponseRedirect(reverse('crud:{}'.format(item)))
    
    context = {'del_item': del_item}

    return render(request, 'crud/delete.html', context)


def products(request):
    context = {'products': Product.objects.all()}

    return render(request, 'crud/products.html', context)

def locations(request):

    context = {'locations': Location.objects.all()}
    
    return render(request, 'crud/locations.html', context)

def shelves(request):

    context = {'shelves': Shelf.objects.all()}
    
    return render(request, 'crud/shelves.html', context)

def inventory(request):

    context = {'inventory': Inventory.objects.all()}
    
    return render(request, 'crud/inventory.html', context)
