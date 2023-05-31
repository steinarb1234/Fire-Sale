from django.db import models
from item.models import Item
from user.models import User



# Create your models for "Offer" here:


class Offer(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_offers', blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_offers')
    amount = models.FloatField(default=0.0)
    status = models.CharField(max_length=255, default="Pending answer")



class OfferDetails(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE, primary_key=True)
    start_date = models.DateField()
    message = models.TextField(max_length=255)


