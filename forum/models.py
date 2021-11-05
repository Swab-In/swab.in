from django.db import models
from lokasi.models import Post
from django.conf import settings

# Create your models here.
class Forum(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    title = models.CharField(max_length=30)
    message = models.TextField()
    image = models.TextField()
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "%s " % (self.title)
