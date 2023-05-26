from django.forms import ModelForm, widgets
from user.models import UserProfile

class userProfileForm(ModelForm):
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