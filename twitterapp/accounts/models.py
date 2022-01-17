from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

from feed.models import tweet
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    image = models.ImageField(default = 'default.PNG',upload_to = 'profile_pics')
    bio = models.TextField(default='')


    def __str__(self):
        return f'{self.user.username}'

    