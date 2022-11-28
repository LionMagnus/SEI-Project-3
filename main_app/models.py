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
  def __str__(self):
    return f'{self.eventTitle} ({self.id})'

  def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})

class Comment(models.Model):
  comment = models.TextField(max_length=1000)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  created_on = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=False)
  class Meta:
    ordering = ['created_on']

