from django import forms
from django.forms import ModelForm
from offer.models import Offer

class CreateOfferForm(ModelForm):
    price = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Offer
        fields = ['amount']
        widgets = {
            'amount': forms.TextInput(attrs={'type': 'number'}),
        }


class CheckOutForm(ModelForm):

    name = forms.CharField(max_length=255)
    street_name = forms.CharField(max_length=255)
    house_number = forms.CharField(max_length=255)
    city = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    postal_code = forms.CharField(max_length=255)
    name_of_cardholder = forms.CharField(max_length=255)
    card_number = forms.CharField(max_length=255)
    expiration_date = forms.CharField(max_length=255)
    cvs = forms.CharField(max_length=255)
