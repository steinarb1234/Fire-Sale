from django import forms
from django.forms import ModelForm, widgets, Form
from offer.models import Offer, OfferDetails
from rating.models import Rating
from user.models import UserProfile


class CreateOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['amount']
        widgets = {
            'amount': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': '0'}),
        }

class CreateOfferDetailsForm(forms.ModelForm):
    class Meta:
        model = OfferDetails
        fields = ['message']
        widgets = {
            'message': widgets.Textarea(attrs={'class': 'form-control'}),
        }


class ContactInformationForm(ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = UserProfile
        fields = ['country', 'address', 'city', 'zip_code']
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'})
        }


class PaymentForm(Form):
    name_of_cardholder = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiration_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'message']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 5}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'min': 0, 'max': 5}),
        }

