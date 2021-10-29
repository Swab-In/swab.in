from django.db import models
from django.conf import settings

class SwabInformation(models.Model):
    nama = models.CharField(max_length=50, default='-')
    price = models.CharField(max_length=30, default='-')
    akurasi = models.CharField(max_length=30, default='-')
    prosedu = models.CharField(max_length=50, default='-')
    deskripsi = models.TextField(max_length=500, default='-')

class VaksinInformation(models.Model):
    nama = models.CharField(max_length=30, default='-')    
    produsen = models.CharField(max_length=30, default='-')
    frekuensi = models.CharField(max_length=30, default='-')
    efikasi = models.CharField(max_length=30, default='-')    
    deskripsi = models.TextField(max_length=500, default='-')

class Experience(models.Model):
    penulis = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    pengalaman = models.TextField(max_length=300)
