from .models import Coffee
from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import gettext_lazy as _


class CoffeeAdd(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('coffee_name', 'origin', 'bean', 'taste_profile', 'roast', 'description')

class CoffeeUpdate(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('coffee_name', 'origin', 'bean', 'taste_profile', 'roast', 'description')

# Extend SIGNUP FORM
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label=_("Your company"),
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _("Coffee Company Ltd")}),
    )
    # about = forms.CharField(
    #     help_text = "Tell us about your business. This will be displayed below your coffee listings.",
    #     widget=forms.Textarea(attrs={"placeholder": _("Founded in 2025, Coffee Company Ltd is... ")}),
    # )

    def save(self, request):
        # Call the parent save method
        user = super(CustomSignupForm, self).save(request)
        
        # Add the first_name to the user model
        user.first_name = self.cleaned_data["first_name"]
        user.save()
        
        return user