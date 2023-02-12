from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem


def greeting(request):
    content_type = ContentType.objects.get_for_model(Product)
    queryset = TaggedItem.objects.filter(
        content_type=content_type,
        object_id=1,
    )
    list(queryset)
    return render(request, "home.html", {"name": "Nina"})
