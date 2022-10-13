from django.db.models import Count
from django.shortcuts import render
from lojavirtual.inventory import models


def home(request):
    return render(request, "index.html")


def category(request):
    data = models.Category.objects.all()

    return render(request, "categories.html", {"data": data})


def product_by_category(request, category):

    data = models.Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "category__name", "product__store_price"
    )

    return render(request, "product_by_category.html", {"data": data})


def product_detail(request, slug):

    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)

    print(filter_arguments)
    data = (
        models.ProductInventory.objects.filter(product__slug=slug)
        .filter(attribute_values__attribute_value__in=filter_arguments)
        .annotate(num_tags=Count("attribute_values"))
        .filter(num_tags=len(filter_arguments))
        .values(
            "id",
            "sku",
            "product__name",
            "store_price",
            "product_inventory__units",
        )
    )
    print(data)

    return render(request, "product_detail.html", {"data": data})
