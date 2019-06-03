"""Models for invoice service."""

from datetime import datetime
from django.db import models


class Invoice(models.Model):
    """Invoice general data."""

    number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """Return number and customer name as string representation."""
        return '{num} {customer}'.format(
            num=self.number,
            customer=self.customer_name
        )


class InvoiceLine(models.Model):
    """Line of an invoice."""

    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def __str__(self):
        """Return quantity and description as string representation."""
        return '{qty} {desc}'.format(
            qty=self.quantity,
            desc=self.description
        )
