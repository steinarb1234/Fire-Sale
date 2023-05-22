from django.db import models
from offer.models import Offer

# Create your "Ratings" models here:

class Rating(models.Model):
    offer = models.OneToOneField(Offer, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.DateField()
    rating = models.IntegerField()