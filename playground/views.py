from django.http import HttpResponse


def greeting(request):
    return HttpResponse("<h1>Good Day</h1>")
