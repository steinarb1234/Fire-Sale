from django.shortcuts import render

categories = [
    {'name': 'Fashion', 'image': 'hat_image'},
    {'name': 'Tech', 'image': 'computer_image'},
    {'name': 'Home', 'image': 'house_image'},
    {'name': 'Toys', 'image': 'toy_image'},
    {'name': 'Sports', 'image': 'sports_image'},
    {'name': 'Books', 'image': 'book_image'},
    {'name': 'Other', 'image': 'other_image'}
]

# Create your views here.


def index(request):
    return render(request, 'category/index.html', context={
        'categories': categories
    })