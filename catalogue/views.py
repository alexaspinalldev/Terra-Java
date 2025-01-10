from django.shortcuts import render
from django.views import generic
from .models import Coffee

# Create your views here.
class CoffeeList(generic.ListView):
    queryset = Coffee.objects.filter(listing_approved=True)
    template_name = "coffee_list.html"
    paginate_by = 12
