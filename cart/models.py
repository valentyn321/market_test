from django.db import models
from django.conf import settings

from decimal import Decimal
from django.core.validators import MinLengthValidator, MinValueValidator


class Product(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=256,
        validators=[MinLengthValidator(2)]
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(('0.01')))]
    )
    description = models.TextField(
        blank=True,
        null=True
    )
