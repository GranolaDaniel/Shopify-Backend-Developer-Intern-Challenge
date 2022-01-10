from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),

    path('<str:item>/add/', views.add, name='add'),
    path('<str:item>/<uuid:id>/', views.edit, name='edit'),
    path('<str:item>/<uuid:id>/delete', views.delete, name='delete'),
 
    path('products/', views.products, name='products'),
    path('locations/', views.locations, name='locations'),
    path('shelves/', views.shelves, name='shelves'),
    path('inventory/', views.inventory, name='inventory'),
]
