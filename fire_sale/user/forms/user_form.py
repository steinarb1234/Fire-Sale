from django.forms import ModelForm, widgets
from django import forms
from user.models import User
from user.models import UserProfile

class CustomUserCreationForm(ModelForm):
    email = forms.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['full_name', 'email']
        
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id']
        # Bæta við database fyrir countries
        widgets = {
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip-code': widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': widgets.TextInput(attrs={'class': 'form-control'}),
            # Atuga með userInfo á þessari síður...
            'user_info': widgets.TextInput(attrs={'class': 'form-control'}),
        }