from django.forms import ModelForm, widgets
from django import forms
from item.models import Item, ItemDetails, ItemStats, ItemImage


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'})

        }


class CreateListingForm(forms.ModelForm):
    condition = forms.CharField(max_length=255)
    description = forms.CharField(max_length=9999, widget=forms.Textarea)
    images = forms.CharField(max_length=9999, widget=forms.Textarea)

    class Meta:
        model = Item
        fields = ['name', 'price', 'condition', 'description', 'images']

class EditListingForm(forms.ModelForm):
    condition = forms.CharField(max_length=255)
    description = forms.CharField(max_length=9999, widget=forms.Textarea)
    images = forms.CharField(max_length=9999, widget=forms.Textarea)

    class Meta:
        model = Item
        fields = ['name', 'price', 'condition', 'description', 'images']