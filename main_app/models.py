from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

class Trip(models.Model):
    
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Meta: 
    ordering = ['name']

class Traveler(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

