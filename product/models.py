from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Product(models.Model):
    CONDITION_TYPE = (
        ("New", "New"),
        ("Used", "Used")
    )
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100, choices=CONDITION_TYPE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.brand_name
