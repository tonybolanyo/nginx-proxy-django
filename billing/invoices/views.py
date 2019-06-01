"""API Views for invoice microservice."""

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Invoice, InvoiceLine
from .serializers import BasicInvoiceSerializer, FullInvoiceSerializer


class InvoiceListAPIView(ListAPIView):
    """Return all invoices."""

    queryset = Invoice.objects.all()
    serializer_class = BasicInvoiceSerializer


class InvoiceDetailAPIView(RetrieveAPIView):
    """Return all invoice data."""

    queryset = Invoice.objects.all()
    serializer_class = FullInvoiceSerializer
