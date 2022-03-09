from django.db import models
from datetime import datetime, date

class Trip(models.Model):
    
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.name

class Meta: 
    ordering = ['name']

