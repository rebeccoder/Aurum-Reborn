from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, default='Anonymous')
    testimonial = models.TextField()
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])


    def __str__(self):
        return self.name
