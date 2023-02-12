from django.shortcuts import render
from django.db.models import Value, F
from store.models import Customer


def greeting(request):
    queryset = Customer.objects.annotate(is_new=Value(True))
    queryset = Customer.objects.annotate(new_id=F('id') + 1)
    list(queryset)
    return render(request, "home.html", {"name": "Nina"})
