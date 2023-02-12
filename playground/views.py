from django.shortcuts import render
from django.db import connection
from store.models import Product


def greeting(request):
    products = Product.objects.raw("SELECT id, title FROM store_product")
    products = Product.objects.raw("SELECT * FROM store_product")
    print(products)
    list(products)

    # Execute SQL queries not tied to a model
    with connection.cursor() as cursor:
        cursor.execute("INSERT ...............")
        cursor.callproc("get_customers", [1, 2, "a"])

    return render(request, "home.html", {"name": "Nina"})
