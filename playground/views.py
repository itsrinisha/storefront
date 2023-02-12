from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def greeting(request):
    queryset = Product.objects.filter(unit_price__gt=20)
    queryset = Product.objects.filter(unit_price__lt=20)
    queryset = Product.objects.filter(unit_price__gte=20)
    queryset = Product.objects.filter(unit_price__lte=20)
    queryset = Product.objects.filter(unit_price__range=(10, 50))

    queryset = Product.objects.filter(collection__id=1)
    queryset = Product.objects.filter(collection__id__range=(1, 2, 3))
    queryset = Product.objects.filter(collection__title="Beauty")

    queryset = Product.objects.filter(title__contains="coffee")
    queryset = Product.objects.filter(title__icontains="coffee")
    queryset = Product.objects.filter(title__startswith="coffee")
    queryset = Product.objects.filter(title__istartswith="coffee")
    queryset = Product.objects.filter(title__endswith="coffee")
    queryset = Product.objects.filter(title__iendswith="coffee")

    queryset = Product.objects.filter(last_update__year=2000)

    queryset = Product.objects.filter(description__isnull=True)
    list(queryset)

    return render(request, "home.html", {"name": "Nina"})
