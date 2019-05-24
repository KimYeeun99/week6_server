from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete='CASCADE')
    message = models.CharField(max_length=140)
    