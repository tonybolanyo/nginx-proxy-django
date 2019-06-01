"""Models for product catalog app."""

from django.db import models


class Product(models.Model):
    """Simple product catalog."""

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """Return product name as string object representation."""
        return self.name
