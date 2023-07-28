from django.db import models

# Create your models here.
from django.db import models

class Creator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    image = models.ImageField(upload_to='creators/', default='default_image.jpg')
    

    def __str__(self):
        return self.name