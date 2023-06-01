#from django.contrib.auth.models import User
from django.db import models


# Create your models here for user.
class User(models.Model):
    full_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

class UserInfo(models.Model):
    image = models.CharField(max_length=9999, blank=True, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Country(models.Model):
    country = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.country


class UserProfile(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    bio = models.CharField(max_length=9999, blank=True)
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE, primary_key=True)


class Notification(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True, null=True)
    href = models.URLField(max_length=255, blank=True, null=True)
    href_parameter = models.CharField(max_length=255, blank=True, null=True)
    datetime = models.DateTimeField()
    seen = models.BooleanField(default=False)
