from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profiles')
    images = models.ImageField(upload_to="profile_pic")
