from django.test import TestCase
from cart.models import Product

class TestModels(TestCase):
    def set_up(self):
        self.product = Product.objects.create(title="New", price="3.99")

    def test_required_fileds(self):
        """Checks, if all required field are present"""
        fields = Product._meta.fields
        required_f = []
        required_f_values = []
        for field in fields:  # checks all required fileds
            if not field.blank:
                required_f.append(str(field))
        for field in required_f_values:
            assert(field in self.product._meta.fields)
