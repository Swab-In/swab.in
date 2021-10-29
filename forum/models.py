from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Forum(models.Model):
    forum_id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.RESTRICT)
    title = models.CharField(max_length=30)
    message = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return "%s " % (self.title)

class Komentar(models.Model):
    forum_id = models.ForeignKey(Forum, on_delete=models.RESTRICT)
    komentar = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    def __str__(self):
        return "%s" % (self.komentar)
