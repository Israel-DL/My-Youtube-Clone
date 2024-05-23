from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=1000)

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username