from django.shortcuts import render
from django.db import connection
from store.models import Product


def greeting(request):
    return render(request, "home.html", {"name": "Nina"})
