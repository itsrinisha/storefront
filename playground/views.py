from django.shortcuts import render
from store.models import Order, OrderItem
from django.db import transaction


# @transaction.atomic()
# def greeting(request):
#     order = Order()
#     order.customer_id = 1
#     order.save()

#     item = OrderItem()
#     item.order = order
#     item.product_id = 20
#     item.quantity = 1
#     item.unit_price = 8
#     item.save()
#     return render(request, "home.html", {"name": "Nina"})


def greeting(request):
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = 20
        item.quantity = 1
        item.unit_price = 8
        item.save()
        return render(request, "home.html", {"name": "Nina"})
