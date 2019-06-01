"""API views for catalog app."""

from rest_framework.generics import ListAPIView

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    """Get all products list."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
