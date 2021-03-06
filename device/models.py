from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
