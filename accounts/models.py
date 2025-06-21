from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser) :
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username
        
class Profile(models.Model) :
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/' , default='avatars/default.png')
    skills = models.CharField(max_length=255 , blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"