"""Serializers for invoice app."""

from rest_framework.serializers import ModelSerializer

from .models import Invoice, InvoiceLine


class BasicInvoiceSerializer(ModelSerializer):
    """Only basic fields of the invoice."""

    class Meta:
        """Serializer definition from model."""

        model = Invoice
        fields = ('id', 'number', 'date', 'customer_name')


class InvoiceLineSerializer(ModelSerializer):
    """Invoice line serializer."""

    class Meta:
        """Serializer definition from model."""

        model = InvoiceLine
        fields = ('id', 'quantity', 'description', 'unit_price', 'subtotal')


class FullInvoiceSerializer(ModelSerializer):
    """Invoice with lines."""

    lines = InvoiceLineSerializer(many=True, read_only=True)

    class Meta:
        """Serializer definition from model."""

        model = Invoice
        fields = ('id', 'number', 'date', 'customer_name', 'lines')
