from django.db import models

# Create your models here.
class Tour(models.Model):
    #we need a country of origin
    #destination, number of nights
    #price for the tour
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_nights = models.IntegerField()
    price_tour = models.IntegerField()
    