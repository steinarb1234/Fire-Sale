from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from category.models import Category
from item.forms.item_form import CreateItemForm, EditItemForm, CreateItemImageForm, CreateItemDetailsForm, \
    EditItemImageForm, EditItemStatsForm, EditItemDetailsForm
from item.models import Item, ItemImage, ItemDetails, ItemStats
from item.service import ItemService

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home/index.html', context={
        'categories_and_items': ItemService.get_categories_and_items_by_userid(request.user.id),
    })


def get_item_details_by_id(request, id):
    return render(request, 'item/item_details.html', {
        'item_details': get_object_or_404(ItemDetails, pk=id),
        'seller_details': ItemService.get_seller_details_from_item_id(id),
        'category_and_items': ItemService.get_category_and_items_by_itemid(id)
    })


@login_required
def create_item(request):
    if request.method == 'POST':
        item_form = CreateItemForm(data=request.POST)
        item_image_form = CreateItemImageForm(data=request.POST)
        item_details_form = CreateItemDetailsForm(data=request.POST)

        # TODO: Logic layer síun á gögnum
        if item_form.is_valid() and item_image_form.is_valid() and item_details_form.is_valid():
            item = item_form.save(commit=False)
            item.seller_id = int(request.user.id)
            item.save()

            item_image = item_image_form.save(commit=False)
            item_image.item_id = item.id
            item_image.save()

            item_stats = ItemStats(item=item)
            item_stats.save()

            item_details = item_details_form.save(commit=False)
            item_details.item_stats_id = item_stats.item_id
            item_details.save()

            return redirect('item-details', item.id)
    else:
        item_form = CreateItemForm()
        item_image_form = CreateItemImageForm()
        item_details_form = CreateItemDetailsForm()

    return render(request, 'item/create_item.html', {
        'item_form': item_form,
        'item_image_form': item_image_form,
        'item_details_form': item_details_form
    })


def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('item-index')


def edit_item(request, id):
    item_instance = get_object_or_404(Item, pk=id)
    item_image_instance = get_object_or_404(ItemImage, item_id=id)
    item_stats_instance = get_object_or_404(ItemStats, pk=id)
    item_details_instance = get_object_or_404(ItemDetails, pk=id)
    if request.method == 'POST':
        item_form = EditItemForm(data=request.POST, instance=item_instance)
        item_image_form = EditItemImageForm(data=request.POST, instance=item_image_instance)
        item_stats_form = EditItemStatsForm(data=request.POST, instance=item_stats_instance)
        item_details_form = EditItemDetailsForm(data=request.POST, instance=item_details_instance)
        if item_form.is_valid() and item_image_form.is_valid():
            item_form.save()
            item_image_form.save()

            return redirect('item-details', id)
    else:
        item_form = EditItemForm(instance=item_instance)
        item_image_form = EditItemImageForm(instance=item_image_instance)
        item_stats_form = EditItemStatsForm(instance=item_stats_instance)
        item_details_form = EditItemDetailsForm(instance=item_details_instance)
    return render(request, 'item/edit_item.html', {
        'item_form': item_form,
        'item_image_form': item_image_form,
        'item_stats_form': item_stats_form,
        'item_details_form': item_details_form,
        'id': id,
    })




