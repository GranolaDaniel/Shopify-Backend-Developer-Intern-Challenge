from django.test import TestCase

from ..forms import ProductForm

class ProdFormTestCase(TestCase):
    def test_prod_positive_validation(self):
        """Verify that the entered price on the form is >=0.01"""
        form = ProductForm()

        form.fields['name'] = 'Test peach'
        form.fields['price'] = 0.0

        self.assertFalse(form.is_valid())