from django.db import models
from creators.models import Creator

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(max_length=100, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    karat = models.CharField(max_length=100)
    creator = models.ForeignKey('creators.Creator', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_images/', default='media/image.jpg')

    def __str__(self):
        return self.name
