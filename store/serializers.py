from decimal import Decimal
from rest_framework import serializers
from .models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "title"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "slug",
            "inventory",
            "unit_price",
            "price_with_tax",
            "collection",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.5)

    # Overrides default create behavior
    def create(self, validated_data):
        product = Product(**validated_data)
        product.collection_id = 2
        product.save()
        return product

    # Overrides default update behavior
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title") + "Apple"
        instance.save()
        return instance
