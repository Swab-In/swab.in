from django.db import models

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=30)
    message = models.TextField()
    image = models.ImageField()
