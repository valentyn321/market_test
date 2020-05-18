from django.views.generic.edit import FormView
from django.shortcuts import render, redirect

from cart.forms import ProductCreationForm


class ProductView(FormView):
    form_class = ProductCreationForm
    template_name = 'cart/create_product.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('create_product')
        else:
            return render(request, self.template_name, {'form': form})
