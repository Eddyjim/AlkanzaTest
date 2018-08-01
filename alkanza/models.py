from django.db import models
from datetime import datetime

# Create your models here.

class Evaluation(models.Model):
    date = models.DateTimeField('date published')
    radius = models.IntegerField()
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    def __init__(self, radius,latitude,longitude):
        self.date = datetime.datetime.now()
        self.radius = radius
        self.latitude = latitude
        self.longitude = longitude

class Point(models.Model):
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    distance = models.IntegerField()
    balanced = models.BooleanField(default=False)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
