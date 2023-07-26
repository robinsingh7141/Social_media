from django.db import models
# from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

from django.contrib.auth.models import User 



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields for user profile (e.g., bio, followers, etc.)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    # Add other fields for post (e.g., likes, comments, etc.)

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}"  # Return a shortened version of the content

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField(max_length=20)
    comment = models.TextField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Signup(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

    def __str__(self):
        return self.username