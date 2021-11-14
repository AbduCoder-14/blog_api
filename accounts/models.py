from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255)
    last_activity = models.DateTimeField()
