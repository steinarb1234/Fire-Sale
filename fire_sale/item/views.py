# Import statements
from django.db.models import Max, Avg
from django.forms import formset_factory
from django.shortcuts import render, get_object_or_404, redirect
from rating.models import Rating
from user.models import UserProfile
from category.models import CategoryViews
from item.forms.item_form import CreateItemForm, EditItemForm, CreateItemImageForm, CreateItemDetailsForm, \
EditItemImageForm, EditItemDetailsForm
from item.models import Item, ItemImage, ItemDetails, ItemStats
from watchlist.models import WatchListItem
from item.service import ItemService
from django.contrib.auth.decorators import login_required
from offer.models import Offer
from django.shortcuts import render
from django.core.exceptions import PermissionDenied



def index(request):
    return render(request, 'home/index.html', context={
        'categories_and_items': ItemService.get_categories_and_items_by_userid(request.user.id),
    })

def get_item_details_by_id(request, id):
    """
    Retrieves and renders the details of an item by its ID.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the item.

    Returns:
        HttpResponse: Renders the 'item/item_details.html' template with the item details and related information.

    Raises:
        Http404: If the item details or item stats do not exist.

    """
    item_details = get_object_or_404(ItemDetails.objects.select_related(
        'item_stats__item',
        'item_stats__item__category',
        'item_stats__item__seller',
        'condition',
    ), pk=id)

    item_stats = get_object_or_404(ItemStats, pk=id)
    item_stats.views += 1
    item_stats.save()

    if request.user.id:
        category_views = get_object_or_404(CategoryViews, user=request.user.id, category=item_stats.item.category)
        category_views.category_views += 1
        category_views.save()

    seller_id = item_details.item_stats.item.seller_id
    user_location = UserProfile.objects.get(user_info__user_id=seller_id).country

    try:
        user_rating = round(Rating.objects.filter(offer_id__seller=seller_id).aggregate(Avg('rating'))['rating__avg'], 1)
    except TypeError:
        user_rating = '(No ratings)'

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
    """
    Creates a new item.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: If the request method is POST and the form data is valid, redirects to the item details page of the created item.
        Otherwise, renders the 'item/create_item.html' template with the item creation forms.

    """
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
    """
    Deletes an existing item.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the item to delete.

    Returns:
        HttpResponse: Redirects to the 'my-listings' page after deleting the item.

    Raises:
        Http404: If the item does not exist or does not belong to the current user.

    """
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('my-listings')

@login_required
def edit_item(request, id):
    """
    Edits an existing item.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the item to edit.

    Returns:
        HttpResponse: If the request method is POST and the form data is valid, redirects to the item details page of the edited item.
        Otherwise, renders the 'item/edit_item.html' template with the item edit forms.

    Raises:
        PermissionDenied: If the item does not belong to the current user.
        Http404: If the item or item details do not exist.

    """
    ItemImageFormSet = formset_factory(EditItemImageForm, extra=1, max_num=10, absolute_max=50, can_delete=True)

    item_instance = get_object_or_404(Item, pk=id)
    item_image_instances = ItemImage.objects.filter(item_id=id)
    item_details_instance = get_object_or_404(ItemDetails, pk=id)

    if item_instance.seller.id != request.user.id:
            raise PermissionDenied()
    else:
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

@login_required()
def item_offers(request, item_id):
    """
    Renders the offers for a specific item.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item.

    Returns:
        HttpResponse: Renders the 'offer/item_offers.html' template with the offers and the associated item.

    Raises:
        PermissionDenied: If the item does not belong to the current user.
        Http404: If the item does not exist.

    """
    offers = Offer.objects.filter(item_id=item_id).order_by('-amount')
    item = Item.objects.get(pk=item_id)
    if item.seller.id != request.user.id:
            raise PermissionDenied()
    else:
        return render(request, 'offer/item_offers.html', {
            "offers": offers,
            "item": item,
    })

@login_required
def item_offers_buyers(request, item_id):
    """
    Renders the offers for a specific item from the buyer's perspective.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item.

    Returns:
        HttpResponse: Renders the 'offer/item_offers_buyer_view.html' template with the offers and the associated item.

    Raises:
        Http404: If the item does not exist.

    """
    offers = Offer.objects.filter(item_id=item_id).order_by('-amount')
    item = Item.objects.get(pk=item_id)

    return render(request, 'offer/item_offers_buyer_view.html', {
        "offers": offers,
        "item": item,
    })



