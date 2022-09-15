from django.contrib.auth.models import User
from django.db import models


class Phone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, blank=True)
