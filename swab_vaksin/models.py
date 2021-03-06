from django.db import models
from django.conf import settings

class SwabInformation(models.Model):
    nama = models.CharField(max_length=25, default='-')
    price = models.CharField(max_length=30, default='-')
    akurasi = models.CharField(max_length=30, default='-')
    prosedur = models.CharField(max_length=50, default='-')
    deskripsi = models.TextField(max_length=500, default='-')
    gambar = models.ImageField(upload_to='static/images/', default='static\images\iSwab.jpg')

class VaksinInformation(models.Model):
    nama = models.CharField(max_length=25, default='-')    
    produsen = models.CharField(max_length=30, default='-')
    frekuensi = models.CharField(max_length=30, default='-')
    efikasi = models.CharField(max_length=30, default='-')    
    deskripsi = models.TextField(max_length=500, default='-')
    gambar = models.ImageField(upload_to='static/images/', default='static\images\iVaksin.jpg')

class SwabExperience(models.Model):
    swab_id = models.ForeignKey(SwabInformation, on_delete=models.RESTRICT)
    penulis = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username'
    )
    pengalamanSwab = models.TextField(max_length=300)

class VaksinExperience(models.Model):
    vaksin_id = models.ForeignKey(VaksinInformation, on_delete=models.RESTRICT)
    penulis = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username'
    )
    pengalamanVaksin = models.TextField(max_length=300)
