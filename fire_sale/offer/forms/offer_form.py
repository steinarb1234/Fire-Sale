from django import forms
from django.forms import ModelForm, widgets
from offer.models import Offer
from user.models import UserProfile

class CreateOfferForm(forms.ModelForm):
    
    message = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Offer
        exclude = ['item', 'buyer', 'seller']
        widgets = {
            'amount': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class CheckoutForm(ModelForm):
    
    name_of_cardholder = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    card_number = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    expiration_date = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cvs = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = UserProfile
        exclude = ['bio', 'user_info']
        widget = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'})
        }   
           
