from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Delete not use field
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
