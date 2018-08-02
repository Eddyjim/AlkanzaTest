from django.conf import settings
import urllib.request
import json

class Evaluator:
    endpointSearch = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    endpointDistance = 'http://maps.google.com/maps/api/js?sensor=false&libraries=geometry?'
    type = 'hospital'

    def findNearPoints(lat, lng):
        location = evaluation.latitude+','+evaluation.longitude
        radius = evaluation.radius
        key = getattr(settings, "GOOGLE_API_KEY", None)
        requestParam = 'location={}&radius={}&type={}&key={}'.format(location,
                                                                      radius,
                                                                      type,
                                                                      key)
        response = urlopen(endpointSearch+requestParam).read()

    
    def calculateCoeficient(distances):
        # This method is a dinamic program to this recurrent function that calculates
        # the disbalanced coeficient:
        # f [x] = x
        # f(x:xs) = |x-y|
        # f(x:xs:y) = minimumx( | f(x) - f(xs:z) | , | f(xs) - f(x:z) | , | f(x) + f(xs) + f(z) | )
        laux = []

        if len(distances) == 1:
            coeficient = li[0]
        elif len(distances) == 2:
            coeficient = abs(distances[0]-distances[1])
        else:
            tempSum = 0
            for i in distances:
                ls = []
                if len(laux) == 0:
                    ls.append(i)
                elif li.index(i) > 1:
                    for j in laux:
                        ls.append(j+i)
                        ls.append(abs(j-i))
            ls.append(abs(temp-i))
        laux = ls
        tempSum = tempSum+i
        coeficient = min(laux)
        return coeficient
