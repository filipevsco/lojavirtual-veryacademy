from rest_framework import serializers

from lojavirtual.inventory.models import Product, ProductInventory


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only = True
