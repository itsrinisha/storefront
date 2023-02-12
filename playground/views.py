from django.shortcuts import render
from django.db.models.functions import Concat
from django.db.models import Value, F, Func
from store.models import Customer


def greeting(request):
    queryset = Customer.objects.annotate(
        full_name=Func(F("first_name"), Value(" "), F("last_name"), function="CONCAT")
    )
    queryset = Customer.objects.annotate(
        full_name=Concat("first_name", Value(" "), "last_name")
    )
    list(queryset)
    return render(request, "home.html", {"name": "Nina"})
