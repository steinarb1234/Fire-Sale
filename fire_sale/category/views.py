from django.shortcuts import render

categories = [
    {'name': 'Fashion', 'image': 'hat_image'},
    {'name': 'Tech', 'image': 'computer_image'},
]

# Create your views here.


def index(request):
    return render(request, 'category/index.html', context={
        'categories': categories
    })
