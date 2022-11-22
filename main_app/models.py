from django.db import models
from django_google_maps import fields as map_fields
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=40)
  age = models.IntegerField()
  location = models.CharField(max_length=30)

class Event(models.Model):
  eventTitle = models.CharField(max_length=100)
  description = models.TextField(max_length=2000)
  date = models.DateField('Event Date')
  evtLocation = models.CharField(max_length=50)

class Rental(models.Model):
  address = map_fields.AddressField(max_length=200)
  geolocation = map_fields.GeoLocationField(max_length=100)