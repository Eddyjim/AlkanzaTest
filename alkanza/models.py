from django.db import models

# Create your models here.

class Evaluation(models.Model):
    date = models.DateTimeField('date published')
    radius = models.IntegerField()
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)

class Point(models.Model):
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    distance = models.IntegerField()
    balanced = models.BooleanField(default=False)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
