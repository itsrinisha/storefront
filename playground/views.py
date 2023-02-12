from django.shortcuts import render
from store.models import Product
from tags.models import TaggedItem


def greeting(request):
    queryset = TaggedItem.objects.get_tags_for(Product, 10)
    list(queryset)
    return render(request, "home.html", {"name": "Nina"})
