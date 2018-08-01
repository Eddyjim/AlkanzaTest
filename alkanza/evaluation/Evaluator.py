from django.conf import settings
import urllib.request
import json

class Evaluator:
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    type = 'hospital'

    def findNearPoints(evaluation):
            location = evaluation.latitude+','+evaluation.longitude
            radius = evaluation.radius
            key = getattr(settings, "GOOGLE_API_KEY", None)
            requestParam = 'location={}&radius={}}&type={}&key={}'.format(location,radius,type,key)
            response = urlopen(endpoint+requestParam).read()
