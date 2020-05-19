from django.test import TestCase, Client
from django.urls import reverse

from cart.models import Product


class TestModels(TestCase):
    def set_up(self):
        self.product = Product.objects.create(title="New", price="3.99")

    def test_required_fileds(self):
        """Checks, if all required field are present"""
        fields = Product._meta.fields
        required_f = []
        required_f_values = []
        for field in fields:
            if not field.blank:
                required_f.append(str(field))
        for field in required_f_values:
            assert(field in self.product._meta.fields)


class TestViewsCart(TestCase):
    def test_productcreate(self):
        """Here we check our view ProductCreate, if it require login"""
        client = Client()
        response = client.get(reverse('create_product'))
        self.assertEqual(response.status_code, 302)