from django.test import TestCase

from ..models import Product, Shelf, Location, Inventory

class ProductTestCase(TestCase):
    #I'm using setUp() instead of setUpTestData() here as the data will be modified and needs to be kept clean between tests
    def setUp(self):
        Product.objects.create(name='Test peach', price=0.75)
    
    def test_prod_created(self):
        """Verify that the product was created and can be read"""
        peach = Product.objects.get(name='Test peach')
        self.assertTrue(Product.objects.filter(name='Test peach').exists())
        self.assertEqual(peach.price, 0.75)
    
    def test_prod_update(self):
        """Verify that the product can be updated/edited"""
        peach = Product.objects.get(name='Test peach')
        peach.price = 0.89
        peach.save()

        self.assertEqual(peach.price, 0.89)
        self.assertTrue(Product.objects.filter(price=0.89).exists())
        self.assertFalse(Product.objects.filter(name=0.75).exists())
    
    def test_prod_deletion(self):
        """Verify that the product can be deleted"""
        peach = Product.objects.get(name='Test peach')

        self.assertTrue(Product.objects.filter(id=peach.id).exists())

        peach.delete()
        self.assertFalse(Product.objects.filter(id=peach.id).exists())

class ShelfTestCase(TestCase):
    def setUp(self):
        Location.objects.create(warehouse_name='Test warehouse')
        Shelf.objects.create(shelf_name='Test shelf', warehouse=Location.objects.get(warehouse_name='Test warehouse'))
    
    def test_shelf_created(self):
        """Verify that the shelf was created and can be read"""
        shelf = Shelf.objects.get(shelf_name='Test shelf')
        self.assertTrue(Shelf.objects.filter(shelf_name='Test shelf').exists())
        self.assertEqual(shelf.shelf_name, 'Test shelf')
    
    def test_shelf_update(self):
        """Verify that the shelf can be updated/edited"""
        shelf = Shelf.objects.get(shelf_name='Test shelf')

        shelf.shelf_name = 'Updated test shelf'
        shelf.save()

        self.assertEqual(shelf.shelf_name, 'Updated test shelf')
        self.assertTrue(Shelf.objects.filter(shelf_name='Updated test shelf').exists())
        self.assertFalse(Shelf.objects.filter(shelf_name='Test shelf').exists())
    
    def test_shelf_deletion(self):
        """Verify that the shelf can be deleted"""
        shelf = Shelf.objects.get(shelf_name='Test shelf')
        self.assertTrue(Shelf.objects.filter(id=shelf.id).exists())

        shelf.delete()
        self.assertFalse(Shelf.objects.filter(id=shelf.id).exists())

    def test_shelf_cascade(self):
        """Verify that on_delete=CASCADE works for Shelf on its warehouse attribute"""
        shelf = Shelf.objects.get(shelf_name='Test shelf')
        warehouse = Location.objects.get(warehouse_name='Test warehouse')

        self.assertTrue(Shelf.objects.filter(id=shelf.id).exists())
        self.assertTrue(Location.objects.filter(id=warehouse.id).exists())

        warehouse.delete()
        self.assertFalse(Location.objects.filter(id=warehouse.id).exists())
        self.assertFalse(Shelf.objects.filter(id=shelf.id).exists())

class LocationTestCase(TestCase):
    def setUp(self):
        Location.objects.create(warehouse_name='Test warehouse')
    
    def test_location_created(self):
        """Verify that the location was created and can be read"""
        location = Location.objects.get(warehouse_name='Test warehouse')
        self.assertTrue(Location.objects.filter(warehouse_name='Test warehouse').exists())
        self.assertEqual(location.warehouse_name, 'Test warehouse')
    
    def test_location_update(self):
        """Verify that the location can be updated/edited"""
        location = Location.objects.get(warehouse_name='Test warehouse')
        location.warehouse_name = 'Updated warehouse'
        location.save()

        self.assertEqual(location.warehouse_name, 'Updated warehouse')
        self.assertTrue(Location.objects.filter(warehouse_name='Updated warehouse').exists())
        self.assertFalse(Location.objects.filter(warehouse_name='Test warehouse').exists())

    def test_location_deletion(self):
        """Verify that the location can be deleted"""
        location = Location.objects.get(warehouse_name='Test warehouse')
        self.assertTrue(Location.objects.filter(id=location.id).exists())

        location.delete()
        self.assertFalse(Location.objects.filter(id=location.id).exists())

class InventoryTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Test peach', price=0.75)
        Location.objects.create(warehouse_name='Test warehouse')
        Shelf.objects.create(shelf_name='Test shelf', warehouse=Location.objects.get(warehouse_name='Test warehouse'))
        Inventory.objects.create(stock=50, shelf=Shelf.objects.get(shelf_name='Test shelf'), product=Product.objects.get(name='Test peach'))

    def test_inv_created(self):
        """Verify that the inventory was created and can be read"""
        inv = Inventory.objects.get(product__name='Test peach')
        self.assertTrue(Inventory.objects.filter(id=inv.id).exists())
        self.assertEqual(inv.product.name, 'Test peach')
        self.assertEqual(inv.stock, 50)

    def test_inv_update(self):
        """Verify that the inventory can be updated/edited"""
        inv = Inventory.objects.get(product__name='Test peach')

        inv.product = Product.objects.create(name='Test apple', price=0.35)
        inv.save()

        self.assertEqual(inv.product.name, 'Test apple')
        self.assertFalse(Inventory.objects.filter(product__name='Test peach').exists())
        self.assertTrue(Inventory.objects.filter(product__name='Test apple').exists())

    
    def test_inv_deletion(self):
        """Verify that the inventory can be deleted"""
        inv = Inventory.objects.get(product__name='Test peach')
        self.assertTrue(Inventory.objects.filter(id=inv.id).exists())

        inv.delete()
        self.assertFalse(Inventory.objects.filter(id=inv.id).exists())


    
    def test_inv_cascade_shelf(self):
        """Verify that on_delete=CASCADE works for Inventory on its shelf attribute"""
        inv = Inventory.objects.get(product__name='Test peach')
        shelf = Shelf.objects.get(shelf_name='Test shelf')

        self.assertTrue(Inventory.objects.filter(id=inv.id).exists())
        self.assertTrue(Shelf.objects.filter(id=shelf.id).exists())

        shelf.delete()

        self.assertFalse(Shelf.objects.filter(id=shelf.id).exists())
        self.assertFalse(Inventory.objects.filter(id=inv.id).exists())
        
    
    def test_inv_cascade_product(self):
        """Verify that on_delete=CASCADE works for Inventory on its product attribute"""
        inv = Inventory.objects.get(product__name='Test peach')
        prod = Product.objects.get(name='Test peach')

        self.assertTrue(Inventory.objects.filter(id=inv.id).exists())
        self.assertTrue(Product.objects.filter(id=prod.id).exists())

        prod.delete()

        self.assertFalse(Product.objects.filter(id=prod.id).exists())
        self.assertFalse(Inventory.objects.filter(id=inv.id).exists())
