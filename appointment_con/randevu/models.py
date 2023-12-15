from django.db import models
from datetime import datetime

class Event(models.Model):
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    start_date =models.TimeField()
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.title

