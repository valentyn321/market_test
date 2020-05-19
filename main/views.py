from django.views.generic.list import ListView

from cart.models import Product

class ProductListView(ListView):

    model = Product
    template_name = 'main/main.html'