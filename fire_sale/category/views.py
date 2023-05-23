from django.shortcuts import render

from item.service import ItemService


def display_items_by_category(request, category_name):
    return render(request, 'category/index.html', {
        'category': category_name,
        'item_list': ItemService.get_items_by_category_name(category_name)
    })