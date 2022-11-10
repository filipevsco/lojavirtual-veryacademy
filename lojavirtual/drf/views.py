from rest_framework import mixins, permissions, viewsets

from lojavirtual.drf.serializer import AllProducts
from lojavirtual.inventory.models import Product


class AllProductsViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):

    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
