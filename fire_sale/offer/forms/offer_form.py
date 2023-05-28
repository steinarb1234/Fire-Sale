from django import forms
from django.forms import ModelForm, widgets
from offer.models import Offer, OfferDetails
from user.models import UserProfile


class CreateOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['amount']
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class CreateOfferDetailsForm(forms.ModelForm):
    class Meta:
        model = OfferDetails
        fields = ['end_date', 'message']
        widgets = {
            'end_date': widgets.DateInput(attrs={'class': 'form-control'}),
            'message': widgets.Textarea(attrs={'class': 'form-control'}),
        }


class CheckoutForm(ModelForm):
    name_of_cardholder = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiration_date = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvs = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = UserProfile
        exclude = ['bio', 'user_info']
        widget = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'})
        }   


