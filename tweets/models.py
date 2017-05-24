from django.conf import settings
from django.db import models
# Create your models here.

class Tweet(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140)
    timestamp = models.TimeField(auto_now=True)
    updated = models.TimeField(auto_now=True, )


    def __str__(self):
        return str(self.content)
