from django.shortcuts import render
from django.db.models import ExpressionWrapper, F, DecimalField
from store.models import Product


def greeting(request):
    queryset = Product.objects.annotate(
        new_price=ExpressionWrapper(F("unit_price") * 1.5, output_field=DecimalField())
    )
    list(queryset)
    return render(request, "home.html", {"name": "Nina"})
