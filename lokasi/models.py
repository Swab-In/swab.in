from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    lokasi = models.CharField(max_length=100)
    detail = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    lokasi_pic = models.TextField(default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.lokasi

    def get_absolute_url(self):
        return reverse('lokasi')