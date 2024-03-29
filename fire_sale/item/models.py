import django.utils.timezone
from django.db import models
from django.db.models import Q

from user.models import User
from category.models import Category
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItemStatuses(models.Model):
    status = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.status


class ItemStats(models.Model):
    views = models.IntegerField(default=0)
    status = models.ForeignKey(ItemStatuses, on_delete=models.PROTECT, default="Not sold")
    listing_date = models.DateField(null=True, blank=True, default=django.utils.timezone.now)
    sold_date = models.DateField(null=True, blank=True)
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)



class ItemConditions(models.Model):
    condition = models.CharField(max_length=255, blank=False, primary_key=True)

    def __str__(self):
        return self.condition


class ItemDetails(models.Model):
    condition = models.ForeignKey(ItemConditions, on_delete=models.PROTECT)
    description = models.TextField(max_length=9999, blank=True)
    item_stats = models.OneToOneField(ItemStats, on_delete=models.CASCADE, primary_key=True)


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # image_url = models.ImageField(max_length=9999, blank=True)
    image = models.URLField(max_length=999, blank=True)

