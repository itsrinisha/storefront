from django.shortcuts import render
from store.models import Product, OrderItem


def greeting(request):
    # queryset = Product.objects.values("id", "title", "collection__title")
    # print(queryset)

    # queryset = Product.objects.values_list("id", "title", "collection__title")
    # print(queryset)

    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values("product_id").distinct()
    ).order_by("title")
    list(queryset)

    return render(request, "home.html", {"name": "Nina"})
