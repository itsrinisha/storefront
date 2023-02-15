from decimal import Decimal
from rest_framework import serializers
from .models import Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source="unit_price"
    )
    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    # 1. PrimaryKeyRelatedField
    collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())

    # 2. StringRelatedField
    collection = serializers.StringRelatedField()

    # 3. NestedSerializer
    collection = CollectionSerializer()

    # 4. HyperlinkedRelatedField
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(), view_name="collection-detail"
    )

    def calculate_tax(self, product):
        return product.unit_price * Decimal(1.5)
