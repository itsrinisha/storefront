from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def greeting(request):
    # all
    products = Product.objects.all()
    list(products)

    # get
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass
        
    # filter
    # product = Product.objects.filter(pk=0).first()

    # exists
    # product = Product.objects.filter(pk=0).exists()


    return render(request, "home.html", {"name": "Nina"})
