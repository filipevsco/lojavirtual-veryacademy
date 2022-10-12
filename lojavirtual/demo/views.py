from django.shortcuts import render
from lojavirtual.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    data = models.Product.objects.filter(category__name=category)

    print(data)

    return render(request, "product_by_category.html", {"data": data})
