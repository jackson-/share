from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class MyUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=132, unique=True)

    USERNAME_FIELD = 'email'
