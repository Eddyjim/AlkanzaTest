#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .evaluation import Evaluator
from django.http import JsonResponse
from .models import Point, Evaluation
from datetime import datetime
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

        return JsonResponse(points,safe=False)
    else:
        return JsonResponse({'error': 'something happened'})

def calculate(request):
    if request.method == 'POST':
        req =  request.POST
        print (req)
        points = json.loads(req.get('points'))
        print (points)
        distances = [];
        for i in points:
            distances.append(i.get('distance'))

        #print (points)
        coeficient = Evaluator.calculateCoeficient(distances)
        eval = Evaluation.objects.create(date=datetime.now(),radius=req.get('radius'),latitude=req.get('lat'),longitude=req.get('lng'),result=coeficient)
        eval.save();
        for p in points:
            point = Point.objects.create(latitude=str(p.get('latitude')),longitude=str(p.get('longitude')),name=p.get('name'),distance=p.get('distance'),evaluation=eval)
            point.save()

    return JsonResponse({'coeficient': coeficient },safe=False)
