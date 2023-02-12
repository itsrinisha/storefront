from django.shortcuts import render
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def greeting(request):
    queryset = Product.objects.all()[:5]
    queryset = Product.objects.all()[8:15]
    list(queryset)

    return render(request, "home.html", {"name": "Nina"})
