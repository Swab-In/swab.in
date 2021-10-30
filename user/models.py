from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
# class UserProfile(models.Model):
#     name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     pekerjaan = models.CharField(max_length=50)
#     umur = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
#     re_password = models.CharField(max_length=20)

# class UserProfile(User):
#     pekerjaan = models.CharField(max_length=50, default='DEFAULT VALUE')
#     umur = models.CharField(max_length=30, default='DEFAULT VALUE')


class CustomUser(User):
    pekerjaan = models.CharField(max_length=50)
    umur = models.CharField(max_length=30)
