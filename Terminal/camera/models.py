from django.db import models
from django.contrib.auth.models import User


class Camera(models.Model):
    title = models.CharField(max_length=30)
    ip = models.CharField(max_length=50)
    creationDate = models.DateTimeField(auto_now=True)
