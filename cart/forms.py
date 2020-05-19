from django import forms
from cart.models import Product


class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'price', 'description']
