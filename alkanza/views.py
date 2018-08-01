#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .evaluation import Evaluator

from .models import Evaluation

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
        evaluation = Evaluation(eval['radius'],eval['latitude'],eval['longitude'])
        evaluation.put()
        points = Evaluator.findNearPoints(evaluation)
        return JsonResponse(points)
