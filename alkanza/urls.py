from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate', views.index, name='evaluate'),
    path('calculate', views.indedx, name='calculate')
]
