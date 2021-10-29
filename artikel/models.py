from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length=500)
    foto = models.TextField()
    author = models.CharField(max_length=140)
    isi = models.TextField()

class Komentar(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    komen = models.CharField(max_length=140)