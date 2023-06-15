from django.db import models
from creators.models import Creator

class Product(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)