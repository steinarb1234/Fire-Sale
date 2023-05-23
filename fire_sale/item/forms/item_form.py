from django.forms import ModelForm, widgets
from django import forms
from item.models import Item, ItemDetails, ItemStats, ItemImage


class ItemCreateForm(ModelForm):
    
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'})

        }

class CreateItemForm(forms.ModelForm):
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.ImageField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
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