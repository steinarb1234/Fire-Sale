from django.db import models

# Create your models here.
class ItemCategory(models.Model):
    name = models.CharField(max_length=255)


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    # seller = models.ForeignKey(User, on_delete=models.CASCADE)




