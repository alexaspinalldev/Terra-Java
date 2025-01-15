from .models import Coffee
from django import forms


class CoffeeUpdate(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('coffee_name', 'origin', 'bean', 'taste_profile', 'roast', 'description')