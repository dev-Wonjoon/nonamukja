from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    email = models.EmailField(
            max_length=127,
            unique=True
            )
    nickname = models.CharField(max_length=64)
