#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .evaluation import Evaluator
from django.http import JsonResponse
from .models import Point, Evaluation
import json


def index(request):
    evaluations = Evaluation.objects.order_by('-date')
    template = loader.get_template('alkanza/index.html')
    context = {
        'evaluations': evaluations,
    }
    return HttpResponse(template.render(context, request))
def evaluation(request,evaluation_id):
    try:
        evaluation = Evaluation.objects.get(pk=evaluation_id)
        template = loader.get_template('alkanza/evaluation.html')
        context = {
            'evaluation': evaluation,
        }
    except evaluation.DoesNotExist:
        raise Http404("Evaluation non-existent")
    return HttpResponse(template.render(context, request))

def evaluate(request):
    if request.method == 'POST':
        eval = request.POST
        points = Evaluator.findNearPoints(eval.get('latitude'),eval.get('longitude'),eval.get('radius'))
        #evaluation = Evaluation(eval['radius'],eval['latitude'],eval['longitude'])
        #evaluation.put()

        return JsonResponse(points,safe=False)
    else:
        return JsonResponse({'error': 'something happened'})

def calculate(request):
    if request.method == 'POST':
        req =  json.dumps(request.POST)
        
        distances = [];
        #points = req['points'];
        for i in req['points']:
            distances.append(i.get('distance'))

        #print (points)
        codeficient = Evaluator.calculateCoeficient(req)
        eval = Evaluation(req.get('radius'),req.get('pivot').get('lat'),req.get('pivot').get('lng'),codeficient)
        eval.save();
        for p in points:
            point = Point(p.get('latitude'),p.get('longitude'),p.get('name'),p.get('distance'),eval)
            point.save()

    return JsonResponse({'codeficient': codeficient},safe=False)
