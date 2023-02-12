from django.shortcuts import render
from django.db.models import Count
from store.models import Customer


def greeting(request):
    queryset = Customer.objects.annotate(orders_count=Count("order"))
    list(queryset)
    return render(request, "home.html", {"name": "Nina"})
