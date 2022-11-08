from rest_framework import permissions, viewsets

from lojavirtual.drf.serializer import AllProducts
from lojavirtual.inventory.models import Product


class AllProductsViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()[:10]
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
