from rest_framework import serializers

from lojavirtual.inventory.models import Product


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False
