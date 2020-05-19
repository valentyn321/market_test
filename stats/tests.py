from django.test import TestCase, Client
from django.urls import reverse

from cart.models import Product


class TestViewsStats(TestCase):
    def test_stats(self):
        """Here we check our view StatsTemplateView, if it require login"""
        cl = Client()
        response = cl.get(reverse('stats'))
        self.assertEqual(response.status_code, 302)
