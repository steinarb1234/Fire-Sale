from django.shortcuts import render

from category.models import Category
from item.service import ItemService
from category.service import CategoryService

def index(request):
    return render(request, 'category/all_categories.html', {
        'categories': Category.objects.all().prefetch_related('parent')
    })


def display_items_by_category(request, category_name):
    query = request.GET.get('q')

    item_list = CategoryService.get_search_results(category_name, query)

    return render(request, 'category/index.html', {
        'category': category_name,
        'item_list': item_list,
        'query': query
    })


