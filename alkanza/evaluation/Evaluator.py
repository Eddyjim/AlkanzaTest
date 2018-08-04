from django.conf import settings
import urllib.request
import json



def findNearPoints(lat, lng, radius):
    endpointSearch = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    type = 'hospital'
    location = str(lat)+','+str(lng)
    key = getattr(settings, "GOOGLE_API_KEY", None)
    requestParam = 'location={}&radius={}&type={}&key={}'.format(location,
                                                                  radius,
                                                                  type,
                                                                  key)
    response = urllib.request.urlopen(endpointSearch+requestParam).read()
    result = json.loads(response)
    print (result)
    points = result.get('results')
    responsePoints = []

    for p in points:
        point = {}
        point['lat'] = p.get('geometry')['location']['lat']
        point['lng'] = p.get('geometry')['location']['lng']
        point['name'] = p.get('name')
        point['icon'] = p.get('icon')
        responsePoints.append(point)

    return responsePoints


def calculateCoeficient(distances):
    # This method is a dinamic program to this recurrent function that calculates
    # the disbalanced coeficient:
    # f [x] = x
    # f(x:xs) = |x-y|
    # f(x:xs:y) = minimumx( | f(x) - f(xs:z) | , | f(xs) - f(x:z) | , | f(x) + f(xs) + f(z) | )
    laux = []

    print (distances)

    if len(distances) == 1:
        coeficient = distances[0]
    elif len(distances) == 2:
        coeficient = abs(distances[0]-distances[1])
    else:
        tempSum = 0
        for i in distances:
            ls = []
            if len(laux) == 0:
                ls.append(i)
            elif distances.index(i) > 1:
                for j in laux:
                    ls.append(j+i)
                    ls.append(abs(j-i))
        ls.append(abs(temp-i))
    laux = ls
    tempSum = tempSum+i
    coeficient = min(laux)
    return coeficient
