from django.db import models

# Create your models here.
class Komentar(models.Model):
    komen = models.CharField(max_length=140)