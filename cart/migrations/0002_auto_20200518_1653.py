# Generated by Django 3.0.6 on 2020-05-18 16:53

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=256, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
