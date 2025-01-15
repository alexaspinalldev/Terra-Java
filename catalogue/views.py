from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Coffee
from .forms import CoffeeUpdate

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

def coffee_edit(request, product_ID):
    """
    view to edit a coffee listing. The button is only visible to authenticated users who are also the Coffee Vendor.
    """
    if request.method == "POST":
        queryset = Coffee.objects
        coffee = get_object_or_404(queryset, product_ID=product_ID)
        coffee_update = CoffeeUpdate(data=request.POST)

        if coffee_update.is_valid() and coffee.vendor == request.user:
            coffee = coffee_update.save(commit=False)
            # coffee.listing_approved = False # In production this would be moderated
            coffee.save()
            messages.add_message(request, messages.SUCCESS, 'The listing was updated')
    else:
        messages.add_message(request, messages.ERROR, 'Error updating listing')

    return HttpResponseRedirect(reverse('Coffee detail', args=[product_ID]))



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
