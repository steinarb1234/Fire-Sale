from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=255)
    avg_rating = models.FloatField(default=0.0)
    image = models.CharField(max_length=9999)
    
class UserProfile(models.Model):
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)