from django.forms import ModelForm, widgets
from django import forms
from item.models import Item


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'})
        }


class CreateItemForm(forms.ModelForm):
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Item
        exclude = ['id', 'category', 'seller']
        fields = ['name', 'price']

class EditItemForm(forms.ModelForm):
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'category', 'seller']
        fields = ['name', 'price']