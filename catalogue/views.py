from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Coffee

# Create your views here.
class CoffeeList(generic.ListView):
    queryset = Coffee.objects.filter(listing_approved=True)
    template_name = "coffee_list.html"
    paginate_by = 12

def coffee_detail(request, product_ID):
    queryset = Coffee.objects.filter(listing_approved=True)
    coffee = get_object_or_404(queryset, product_ID=product_ID)

    return render(
        request,
        "coffee_detail.html",
        {"coffee": coffee},
    )
