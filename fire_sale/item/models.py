from django.db import models
from user.models import User
from category.models import Category

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItemStats(models.Model):
    views = models.IntegerField(default=0)
    watchers = models.IntegerField(default=0)
    # offers = models.ForeignKey(Offer, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)


class ItemDetails(models.Model):
    condition = models.CharField(max_length=255, default="noItem")
    description = models.CharField(max_length=9999, blank=True, default="noItem")
    item_stats = models.OneToOneField(ItemStats, on_delete=models.CASCADE, primary_key=True)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, blank=True)

