from rest_framework import viewsets

from lojavirtual.drf.serializer import AllProducts
from lojavirtual.inventory.models import Product


class AllProducts(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = AllProducts
