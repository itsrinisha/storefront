from django.shortcuts import render
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def greeting(request):
    queryset = Product.objects.filter(inventory=F("unit_price"))
    queryset = Product.objects.filter(inventory=F("collection__id"))
    list(queryset)

    return render(request, "home.html", {"name": "Nina"})
