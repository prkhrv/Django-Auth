from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=10,default='')
    Address = models.TextField(max_length=40,default='')
    Blood_Group = models.CharField(max_length=4,default='')
    profession = models.CharField(max_length=20,default='')
    profile_pic = models.ImageField(upload_to='static/propics')

    def __str__(self):
        return self.email
