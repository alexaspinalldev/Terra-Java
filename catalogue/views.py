from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Coffee

# Create your views here.
class CoffeeList(generic.ListView):
    queryset = Coffee.objects.filter(listing_approved=True)
    template_name = "coffee_list.html"
    paginate_by = 16

def coffee_detail(request, product_ID):
    queryset = Coffee.objects.filter(listing_approved=True)
    coffee = get_object_or_404(queryset, product_ID=product_ID)

    return render(
        request,
        "coffee_detail.html",
        {"coffee": coffee,
        "page_title": coffee.coffee_name},
    )

def coffee_delete(request, product_ID):
    """
    view to delete a coffee listing. The button is only visible to authenticated users who are also the Coffee Vendor.
    """
    queryset = Coffee.objects
    coffee = get_object_or_404(queryset, product_ID=product_ID)

    if coffee.vendor == request.user: #Validate the request on the backend
        coffee.delete()
        messages.add_message(request, messages.SUCCESS, 'Your coffee listing was deleted')
    else:
        messages.add_message(request, messages.ERROR, 'Invalid action')

    return HttpResponseRedirect(reverse('Catalogue'))
