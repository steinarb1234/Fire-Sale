from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=255)
    enail = models.CharField(max_length=255)
    
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    avg_rating = models.FloatField(default=0.0)
    image = models.CharField(max_length=9999)
    
class UserProfile(models.Models):
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    address = models.Charfield(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)