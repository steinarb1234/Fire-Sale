from django.shortcuts import render

from category.models import Category

# Create your views here.


def index(request):
    return render(request, 'category/all_categories.html', context={
        'categories': Category.objects.all()
    })



