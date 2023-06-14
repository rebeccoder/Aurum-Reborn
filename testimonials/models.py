from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100, default='Default Title')
    testimonial = models.TextField()
    rating = models.IntegerField()


    def __str__(self):
        return self.name
