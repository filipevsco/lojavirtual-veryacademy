from django.shortcuts import render
from lojavirtual.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})
