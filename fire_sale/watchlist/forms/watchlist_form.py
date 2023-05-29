from django.forms import ModelForm, widgets
from watchlist.models import WatchListItem


class WatchListCreationForm(ModelForm):
    class Meta:
        model = WatchListItem
        fields = ['user', 'item']
        widgets = {
            'user': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'item': widgets.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }

