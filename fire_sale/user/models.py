from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=255)
    avg_rating = models.FloatField(default=0.0)
    image = models.CharField(max_length=9999, blank=True)
    
class UserProfile(models.Model):
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=255, blank=True)