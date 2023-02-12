from django.shortcuts import render
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def greeting(request):
    queryset = Product.objects.order_by("title")
    queryset = Product.objects.order_by("-title")

    queryset = Product.objects.order_by("unit_price", "title")
    queryset = Product.objects.order_by("unit_price", "-title")
    queryset = Product.objects.order_by("-unit_price", "title")
    queryset = Product.objects.order_by("-unit_price", "-title")

    queryset = Product.objects.order_by("title").reverse()
    queryset = Product.objects.filter(collection__id=1).order_by("unit_price")
    list(queryset)

    product = Product.objects.order_by("unit_price")[0]
    product = Product.objects.earliest("unit_price")
    product = Product.objects.latest("unit_price")

    return render(request, "home.html", {"name": "Nina"})
