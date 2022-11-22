from django.db import models
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
