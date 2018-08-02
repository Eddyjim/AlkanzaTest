from django.db import models
from datetime import datetime

# Create your models here.

class Evaluation(models.Model):
    date = models.DateTimeField('date published')
    radius = models.IntegerField()
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    result = models.IntegerField()
    def __init__(self, radius,latitude,longitude,result):
        self.date = datetime.datetime.now()
        self.radius = radius
        self.latitude = latitude
        self.longitude = longitude
        self.result = result

class Point(models.Model):
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    distance = models.IntegerField()
    balanced = models.BooleanField(default=False)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
