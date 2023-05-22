from django.db import models
from user.models import User
from item.models import ItemStats

# Create your models for "Watchlist" here.

class WatchListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(ItemStats, on_delete=models.CASCADE)   