from django.urls import path
from calculadora.views import index

urlpattern = [
    path('calculadora/', index),
];