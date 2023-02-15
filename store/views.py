from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product


@api_view()
def product_list(request):
    return Response("OK")


@api_view()
def product_detail(request, pk):
    return Response(f"Product {pk}")
