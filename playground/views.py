from django.shortcuts import render
from django.db.models.aggregates import Min, Max, Count, Avg, Sum
from store.models import Product


def greeting(request):
    result = Product.objects.aggregate(
        count=Count("id"),
        sum=Sum("unit_price"),
        avg=Avg("unit_price"),
        min=Min("unit_price"),
        max=Max("unit_price"),
    )
    result = Product.objects.filter(collection__id=1).aggregate(
        count=Count("id"),
        sum=Sum("unit_price"),
        avg=Avg("unit_price"),
        min=Min("unit_price"),
        max=Max("unit_price"),
    )
    return render(request, "home.html", {"name": "Nina"})
