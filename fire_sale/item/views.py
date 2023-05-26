from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from category.models import Category
from item.forms.item_form import CreateItemForm, EditItemForm
from item.models import Item, ItemImage, ItemDetails, ItemStats
from item.service import ItemService

from django.contrib.auth.decorators import login_required


def index(request):
    registered_user_id = request.user.id

    return render(request, 'home/index.html', context={
        'categories_and_items': ItemService.get_categories_and_items_by_userid(request.user.id)
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
        form = CreateItemForm(data=request.POST)
        
        # TODO: Logic layer síun á gögnum
        if form.is_valid():
            
            # Save items in inherited model
            item = form.save(commit=False)
            item.seller_id = int(request.user.id)
            item.save()
             
            # Manually save rest of the items
            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()
            
            item_stats = ItemStats(item=item)
            item_stats.save()
            
            item_details = ItemDetails(
                condition=request.POST['condition'],
                description=request.POST['description'],
                item_stats=item_stats
            )
            item_details.save()

            return redirect('item-details', item.id)
    else:
        form = CreateItemForm()
    return render(request, 'item/create_item.html', {
        'form': form
    })

def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('item-index')

def edit_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == 'POST':
        form = EditItemForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('item-details', id)
    else:
        form = EditItemForm(instance=instance)
        print(2)
    return render(request, 'item/edit_item.html', {
        'form': form,
        'id': id
    })




