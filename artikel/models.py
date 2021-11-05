from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Post(models.Model):
    judul = models.CharField(max_length=500)
    foto = models.TextField()
    author = models.CharField(max_length=140)
    isi = models.TextField()

class Komentar(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    komen = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)