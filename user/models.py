from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class CustomUser(User):
    pekerjaan = models.CharField(max_length=50)
    umur = models.CharField(max_length=30)
    userpic = models.TextField(max_length=200)
