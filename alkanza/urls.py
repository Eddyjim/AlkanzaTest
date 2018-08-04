from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate', views.evaluate, name='evaluate'),
    path('calculate', views.calculate, name='calculate')
]
