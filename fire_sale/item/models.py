from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)

class ItemStats(models.Model):
    views = models.IntegerField()           # TENGJA
    watchers = models.IntegerField()        # TENGJA
    # offers = models.ForeignKey(Offer, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)

class ItemDetails(models.Model):
    condition = models.CharField(max_length=255, default="noItem")
    description = models.CharField(max_length=9999, blank=True, default="noItem")
    item_stats = models.OneToOneField(ItemStats, on_delete=models.CASCADE)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999, blank=True)

