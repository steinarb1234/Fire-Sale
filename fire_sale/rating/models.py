import datetime

from django.db import models
from django.utils import timezone
from offer.models import Offer


class Rating(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.DateField(null=True, blank=True, default=timezone.now)
    rating = models.FloatField()
