from django.db.models import Max, Avg
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.models import User

from rating.models import Rating
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
        'condition',
    ), pk=id)

    item_stats = get_object_or_404(ItemStats, pk=id)
    item_stats.views += 1
    item_stats.save()

    seller_id = item_details.item_stats.item.seller_id
    user_location = UserProfile.objects.get(user_info__user_id=seller_id).country
    user_rating = round(Rating.objects.filter(offer_id__seller=seller_id).aggregate(Avg('rating'))['rating__avg'], 1)\
                  or 'No ratings'
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
    CreateItemImageFormSet = formset_factory(CreateItemImageForm, extra=1, max_num=10, absolute_max=50, can_delete=True)

    if request.method == 'POST':
        item_form = CreateItemForm(data=request.POST)
        item_image_formset = CreateItemImageFormSet(data=request.POST)
        item_details_form = CreateItemDetailsForm(data=request.POST)

        if item_form.is_valid() and item_image_formset.is_valid() and item_details_form.is_valid():
            item = item_form.save(commit=False)
            item.seller_id = int(request.user.id)
            item.save()

            for form in item_image_formset:
                if form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.item = item
                    image.save()

            item_stats = ItemStats(item=item)
            item_stats.save()

            item_details = item_details_form.save(commit=False)
            item_details.item_stats_id = item_stats.item_id
            item_details.save()

            return redirect('item-details', item.id)
    else:
        item_form = CreateItemForm()
        item_image_formset = CreateItemImageFormSet()
        item_details_form = CreateItemDetailsForm()

    return render(request, 'item/create_item.html', {
        'item_form': item_form,
        'item_image_formset': item_image_formset,
        'item_details_form': item_details_form,
    })


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('item-index')

@login_required
def edit_item(request, id):
    ItemImageFormSet = formset_factory(EditItemImageForm, extra=1, max_num=10, absolute_max=50, can_delete=True)

    item_instance = get_object_or_404(Item, pk=id)
    item_image_instances = ItemImage.objects.filter(item_id=id)
    item_details_instance = get_object_or_404(ItemDetails, pk=id)

    if request.method == 'POST':
        item_form = EditItemForm(data=request.POST, instance=item_instance)
        item_image_formset = ItemImageFormSet(data=request.POST)

        item_details_form = EditItemDetailsForm(data=request.POST, instance=item_details_instance)

        if item_form.is_valid() and item_image_formset.is_valid() and item_details_form.is_valid():
            item = item_form.save()

            # Update or create image instances
            for form, image_instance in zip(item_image_formset.forms, item_image_instances):
                if form.cleaned_data.get('DELETE'):
                    image_instance.delete()
                elif form.cleaned_data.get('image'):
                    image_instance.image_url = form.cleaned_data['image']  # Update the image URL field
                    image_instance.save()

            # Save any new images
            for form in item_image_formset.extra_forms:
                if form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.item = item
                    image.save()

            item_details_form.save()

            return redirect('item-details', id)
    else:
        item_form = EditItemForm(instance=item_instance)
        item_image_formset = ItemImageFormSet(initial=[{'image': image.image} for image in item_image_instances])
        item_details_form = EditItemDetailsForm(instance=item_details_instance)

    return render(request, 'item/edit_item.html', {
        'item_form': item_form,
        'item_image_formset': item_image_formset,
        'item_details_form': item_details_form,
        'id': id,
    })

        # item_form = EditItemForm(data=request.POST, instance=item_instance)
        # item_image_form = EditItemImageForm(data=request.POST, instance=item_image_instance)
        # item_stats_form = EditItemStatsForm(data=request.POST, instance=item_stats_instance)
        # item_details_form = EditItemDetailsForm(data=request.POST, instance=item_details_instance)
        # if item_form.is_valid() and item_image_form.is_valid() and item_stats_form.is_valid() and \
        #         item_details_form.is_valid():
        #     item_form.save()
        #     item_image_form.save()
        #     item_stats_form.save()
        #     item_details_form.save()

        #     return redirect('item-details', id)
    # else:
    #     item_form = EditItemForm(instance=item_instance)
    #     item_image_form = EditItemImageForm(instance=item_image_instance)
    #     item_stats_form = EditItemStatsForm(instance=item_stats_instance)
    #     item_details_form = EditItemDetailsForm(instance=item_details_instance)
    # return render(request, 'item/edit_item.html', {
    #     'item_form': item_form,
    #     'item_image_form': item_image_form,
    #     'item_stats_form': item_stats_form,
    #     'item_details_form': item_details_form,
    #     'id': id,
    # })



@login_required()
def item_offers(request, item_id):
    offers = Offer.objects.filter(item_id=item_id)
    item = Item.objects.get(pk=item_id)
    return render(request, 'offer/item_offers.html', {
        "offers": offers,
        "item": item,
    })

@login_required
def item_offers_buyers(request, item_id):
    offers = Offer.objects.filter(item_id=item_id)
    item = Item.objects.get(pk=item_id)
    return render(request, 'offer/item_offers_buyer_view.html', {
        "offers": offers,
        "item": item,
    })
