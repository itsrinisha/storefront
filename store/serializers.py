from decimal import Decimal
from rest_framework import serializers
from .models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, collection):
        return collection.products.count()

    class Meta:
        model = Collection
        fields = ["id", "title", "products_count"]


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

    # Object Level Validation
    def validate(self, product):
        if product["title"] != "Apple":
            raise serializers.ValidationError("Name should start with Apple")
        return product

    # Field Level Valdation
    def validate_unit_price(self, unit_price):
        if unit_price < 100:
            raise serializers.ValidationError("Price should be more than 100")
        return unit_price
