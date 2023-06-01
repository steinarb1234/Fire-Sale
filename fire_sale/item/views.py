from django.db.models import Max
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from user.models import UserProfile, UserInfo
from category.models import Category
from item.forms.item_form import CreateItemForm, EditItemForm, CreateItemImageForm, CreateItemDetailsForm, \
EditItemImageForm, EditItemStatsForm, EditItemDetailsForm
from item.models import Item, ItemImage, ItemDetails, ItemStats
from watchlist.models import WatchListItem
from item.service import ItemService
from django.contrib.auth.decorators import login_required
from offer.models import Offer


def index(request):
    return render(request, 'home/index.html', context={
        'categories_and_items': ItemService.get_categories_and_items_by_userid(request.user.id),
    })


def get_item_details_by_id(request, id):
    item_details = get_object_or_404(ItemDetails.objects.select_related(
        'item_stats__item',
        'item_stats__item__category',
        'item_stats__item__seller',
        'condition'
    ), pk=id)

    seller_id = item_details.item_stats.item.seller_id
    user_location = UserProfile.objects.get(user_info__user_id=seller_id).country
    user_rating = UserInfo.objects.get(user__id=seller_id).avg_rating
    item = item_details.item_stats.item
    category_and_items = ItemService.get_category_and_items_by_itemid(item.category, id, request.user.id)
    item_images = ItemImage.objects.filter(item=item).select_related('item')
    watchlist_items = WatchListItem.objects.filter(item=item_details.item_stats)
    highest_price = Offer.objects.filter(item_id=id).aggregate(Max('amount'))['amount__max'] or 0

    return render(request, 'item/item_details.html', {
        'user_location': user_location,
        'user_rating' : user_rating,
        'item_details': item_details,
        'category_and_items': category_and_items,
        'item_images': item_images,
        'watchlist_items': watchlist_items,
        'in_watchlist': watchlist_items.exists(),
        'highest_price': highest_price,
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

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('item-index')

@login_required
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
        if item_form.is_valid() and item_image_form.is_valid() and item_stats_form.is_valid() and \
                item_details_form.is_valid():
            item_form.save()
            item_image_form.save()
            item_stats_form.save()
            item_details_form.save()

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


def item_offers(request, item_id):
    offers = Offer.objects.filter(item_id=item_id)
    item = Item.objects.get(pk=item_id)
    return render(request, 'offer/item_offers.html', {
        "offers": offers,
        "item": item,
    })

def item_offers_buyers(request, item_id):
    offers = Offer.objects.filter(item_id=item_id)
    item = Item.objects.get(pk=item_id)
    return render(request, 'offer/item_offers_buyer_view.html', {
        "offers": offers,
        "item": item,
    })

# def input_url_view(request):
#     UrlFormSet = modelformset_factory(ItemImage, form=CreateItemImageForm, extra=1)
#     if request.method == 'POST':
#         formset = UrlFormSet(request.POST)
#         if formset.is_valid():
#             formset.save()
#             # You can add a message or redirect here
#     else:
#         formset = UrlFormSet(queryset=ItemImage.objects.none())
#
#     return render(request, 'item/create_item.html', {'formset': formset})

