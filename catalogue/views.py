from django.shortcuts import render
from django.views import generic
from .models import Coffee

# Create your views here.
class CoffeeList(generic.ListView):
    model = Coffee
