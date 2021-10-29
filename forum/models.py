from django.db import models

# Create your models here.
class Komentar(models.Model):
    komentar = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    