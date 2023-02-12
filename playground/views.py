from django.shortcuts import render
from store.models import Collection, Product


def greeting(request):
    collection = Collection()
    collection.title = "Beauty"
    collection.featured_product = Product(pk=1)
    collection.save()

    collection = Collection(title="Jewelry", featured_product_id=2)
    collection.save()

    collection = Collection.objects.create(title="Games",featured_product_id=3)

    return render(request, "home.html", {"name": "Nina"})
