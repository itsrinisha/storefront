from django.shortcuts import render
from store.models import Collection, Product


def greeting(request):
    collection = Collection(pk=11)
    collection.title = "Makeup"
    collection.featured_product = Product(pk=1)
    collection.save()

    collection = Collection(pk=12)
    collection.featured_product = Product(pk=2)
    # sets title to "", causes data loss
    collection.save()

    collection = Collection.objects.get(pk=13)
    collection.featured_product = Product(pk=3)
    # doesnt set title to ""
    collection.save()

    collection = Collection.objects.filter(pk=14).update(featured_product_id=4)

    return render(request, "home.html", {"name": "Nina"})
