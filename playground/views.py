from django.shortcuts import render
from store.models import Collection


def greeting(request):
    collection = Collection(pk=1)
    collection.delete()

    collection = Collection.objects.filter(id__gt=2).delete()

    return render(request, "home.html", {"name": "Nina"})
