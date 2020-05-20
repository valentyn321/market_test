from django.shortcuts import render, redirect
from django.db.models import Max, Avg, Sum
from django.views.generic.base import TemplateView
from django.db.models.functions import Length

from cart.models import Product


class StatsTemplateView(TemplateView):

    template_name = 'stats/stats.html'

    def get(self, request, *args, **kwargs):

        my_items = Product.objects.filter(
            author=request.user).count()

        all_items = Product.objects.count()

        my_max_price = Product.objects.filter(
            author=request.user).aggregate(Max('price'))['price__max']
        if my_max_price is None:
            my_max_price = 0
        else:
            my_max_price = round(my_max_price, 2)

        averege_price = Product.objects.aggregate(Avg('price'))['price__avg']
        if averege_price is None:
            averege_price = 0
        else:
            averege_price = round(averege_price, 2)

        my_sum = Product.objects.filter(
            author=request.user).aggregate(Sum('price'))['price__sum']
        if my_sum is None:
            my_sum = 0
        else:
            my_sum = round(my_sum, 2)

        my_sum_nude = Product.objects.filter(
            author=request.user)

        title_gt3 = Product.objects.annotate(alias=Length('title')).filter(alias__gt=3)

        price_gt50 = Product.objects.filter(title__gt=3)

        special = (my_sum_nude&title_gt3|price_gt50).aggregate(Sum('price'))['price__sum']

        context = {
            'my_items': my_items,
            'all_items': all_items,
            'my_max_price': my_max_price,
            'averege_price': averege_price,
            'my_sum': my_sum,
            'special': special,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        my_objs = Product.objects.filter(author=request.user)
        for obj in my_objs:
            obj.price += 1
            obj.save()

        return redirect("stats")
