from rest_framework import serializers

from lojavirtual.inventory.models import (
    Brand,
    Product,
    ProductAttributeValue,
    ProductInventory,
)


class ProductAttributeValueSeriealizer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]
        depth = 2


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)
    attribute = ProductAttributeValueSeriealizer(
        source="attribute_values", many=True
    )

    class Meta:
        model = ProductInventory
        fields = [
            "sku",
            "store_price",
            "is_default",
            "product",
            "product_type",
            "brand",
            "attribute",
        ]
        read_only = True
