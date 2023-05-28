from django.forms import ModelForm, widgets
from django import forms
from item.models import Item, ItemDetails, ItemStats, ItemImage



class CreateItemForm(ModelForm):
    # image = forms.ImageField()
    # condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Item
        exclude = ['id', 'seller']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'})
        }


class CreateItemImageForm(ModelForm):
    class Meta:
        model = ItemImage
        widgets = {
            'image': widgets.URLInput(attrs={'class': 'form-control'})
        }
        fields = ['image']


class CreateItemDetailsForm(ModelForm):
    class Meta:
        model = ItemDetails
        widgets = {
            'condition': widgets.Select(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'})
        }
        fields = ['condition', 'description']


class EditItemForm(forms.ModelForm):
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'category', 'seller']
        fields = ['name', 'price']



