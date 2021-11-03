from django.db import models

# Create your models here.
class Pesan(models.Model):
    first = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    no_hp = models.CharField(max_length=30)
    message = models.CharField(max_length=1000)