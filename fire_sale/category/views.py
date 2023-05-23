from django.shortcuts import render

from category.models import Category

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
    # return render(request, 'category/all_categories.html', context={
    #     'categories': categories
    # })

    return render(request, 'category/all_categories.html', context={
        'categories': Category.objects.all()
    })

