from django.db import models

class Informasi(models.Model):
    pengalaman = models.TextField(max_length=500)