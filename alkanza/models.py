from django.db import models

# Create your models here.

class Evaluation(models.Model):
    date = models.DateTimeField('date published')
    name = models.CharField(max_length=100,default='Evaluation')

class PointType(models.Model):
    name = models.CharField(max_length=20,default='Tipo')

class Point(models.Model):
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    type = models.ForeignKey(PointType, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
