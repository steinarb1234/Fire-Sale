from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)

class ItemStats(models.Model):
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    views = models.IntegerField()           # TENGJA
    watchers = models.IntegerField()        # TENGJA
    # offers = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)

class ItemDetails(models.Model):
    item_stats = models.ForeignKey(ItemStats, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    description = models.CharField(max_length=9999, blank=True)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, blank=True)

