from django.shortcuts import render


def greeting(request):
    return render(request, "home.html", {"name": "Nina"})
