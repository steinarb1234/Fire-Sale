from django.shortcuts import render
from item.models import Item


# Create your views here.
def index(request):
    return render(request, 'listing/index.html', context={
        'items': Item.objects.all()
    })