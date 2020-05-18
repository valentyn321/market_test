from django.db import models
from django.conf import settings

class Product(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True, null=True)
