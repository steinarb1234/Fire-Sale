from django.forms import ModelForm, widgets
from django import forms
from user.models import User, UserProfile, UserInfo


class CustomUserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email']
        widgets = {
            'full_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['id', 'user_info']
        # Bæta við database fyrir countries
        widgets = {
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'}),
            'bio': widgets.Textarea(attrs={'class': 'form-control'}),
        }


class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'user_name', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        

class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'country', 'address', 'city', 'zip_code']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'})
        }


class UserInfoUpdateForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['image']
        widgets = {
            'image URL': forms.URLInput(attrs={'class': 'form-control'}),
        }


# For Checkout Form


class CheckOutUserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CheckOutProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['country', 'city' ,'address', 'zip_code']
        widgets = {
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip_code': widgets.TextInput(attrs={'class': 'form-control'})
        }
