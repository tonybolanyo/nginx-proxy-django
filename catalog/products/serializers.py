"""Serializers for product catalog."""

from rest_framework.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):
    """Product serializer with all product fields."""

    class Meta:
        """Basic model serializer definition."""

        model = Product
        fields = ('id', 'name', 'description', 'price')
