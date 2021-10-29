from django.db import models
from django.conf import settings
# Create your models here.
class Forum(models.Model):
    writer = models.ForeignKey(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=30)
    message = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return "%s " % (self.title)

class Komentar(models.Model):
    forum_id = models.ForeignKey(Forum, on_delete=models.RESTRICT)
    komentar = models.TextField()
    user_id = models.ForeignKey(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    
    def __str__(self):
        return "%s" % (self.komentar)
