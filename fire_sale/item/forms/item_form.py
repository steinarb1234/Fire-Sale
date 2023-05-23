from django.forms import ModelForm, widgets
from django import forms
from item.models import Item, ItemDetails, ItemStats, ItemImage


<<<<<<< HEAD
class CreateItemForm(ModelForm):
    image = forms.URLField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
=======
class ItemCreateForm(ModelForm):
    
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
>>>>>>> 0e5f1d32211c5c1a75e25bb45225c2b94a76f4c4
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'price': widgets.NumberInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'})
        }

<<<<<<< HEAD
=======
class CreateItemForm(forms.ModelForm):
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.ImageField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Item
        exclude = ['id', 'category', 'seller']
        fields = ['name', 'price']
>>>>>>> 0e5f1d32211c5c1a75e25bb45225c2b94a76f4c4

class EditItemForm(forms.ModelForm):
    condition = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    images = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Item
        exclude = ['id', 'category', 'seller']
        fields = ['name', 'price']