from django.shortcuts import render

items = [
    {'name': 'Sun hat', 'price': 12345.0},
    {'name': 'Leather Shoes', 'price': 12345.0},
]




# Create your views here.
def index(request):
    return render(request, 'listing/index.html', context={
        'items': items
    })