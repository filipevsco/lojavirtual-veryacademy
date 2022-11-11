from rest_framework import serializers

from lojavirtual.inventory.models import (
    Brand,
    Media,
    Product,
    ProductAttributeValue,
    ProductInventory,
)


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True

    def get_img_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.img_url.url)


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
    image = MediaSerializer(source="media_product_invetory", many=True)

    class Meta:
        model = ProductInventory
        fields = [
            "sku",
            "image",
            "store_price",
            "is_default",
            "product",
            "product_type",
            "brand",
            "attribute",
        ]
        read_only = True
