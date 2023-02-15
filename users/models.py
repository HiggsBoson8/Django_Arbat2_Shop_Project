from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Электронное письмо должно содержать действительный адрес электроннной почты') 
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(models.Model):
    email = models.CharField(max_length = 255, unique = True)
    username = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    code = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager() 

    def __str__(self):
        return self.username + ' ' + self.email
    