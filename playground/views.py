from django.shortcuts import render
from store.models import Product


def greeting(request):
    queryset = Product.objects.only("id", "title", "collection__title")
    print(queryset)

    queryset = Product.objects.defer("description")
    print(queryset)

    return render(request, "home.html", {"name": "Nina"})
