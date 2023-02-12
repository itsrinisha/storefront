from django.shortcuts import render
from store.models import Product, Order


def greeting(request):
    queryset = Product.objects.select_related("collection").all()
    queryset = Product.objects.prefetch_related("promotions").all()
    queryset = (
        Product.objects.select_related("collection")
        .prefetch_related("promotions")
        .all()
    )

    # Get the last 5 orders with their customer and items
    queryset = (
        Order.objects.select_related("customer")
        .prefetch_related("orderitem_set__product")
        .order_by("-placed_at")[:5]
    )
    list(queryset)

    return render(request, "home.html", {"name": "Nina"})
