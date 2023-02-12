from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def greeting(request):
    queryset = Product.objects.filter(inventory__gt=10, unit_price__gt=20)
    queryset = Product.objects.filter(inventory__gt=10).filter(unit_price__gt=20)

    queryset = Product.objects.filter(Q(inventory__gt=10) & Q(unit_price__gt=10))
    queryset = Product.objects.filter(Q(inventory__gt=10) | Q(unit_price__gt=10))
    queryset = Product.objects.filter(Q(inventory__gt=10) & ~Q(unit_price__gt=10))

    list(queryset)

    return render(request, "home.html", {"name": "Nina"})
