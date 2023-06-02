# Import statements
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchListItem
from .forms.watchlist_form import WatchListCreationForm
from item.models import Item
from django.db.models import Exists, OuterRef


@login_required
def add_to_watchlist(request, item_id):
    """
    Adds an item to the user's watchlist.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item to add to the watchlist.

    Returns:
        HttpResponse: If the request method is POST, saves the item to the watchlist and redirects to the item details page.
        Otherwise, redirects to the item details page.

    """
    if request.method == 'POST':
        print('posting')
        watchlist_form = WatchListCreationForm()
        watchlist = watchlist_form.save(commit=False)
        watchlist.item_id = item_id
        watchlist.user_id = request.user.id
        watchlist.save()
        return redirect('item-details', id=item_id)

    return redirect('item-details', id=item_id)


@login_required
def delete_from_watchlist(request, item_id):
    """
    Removes an item from the user's watchlist.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item to remove from the watchlist.

    Returns:
        HttpResponse: Redirects to the item details page after deleting the item from the watchlist.

    Raises:
        Http404: If the watchlist item does not exist or does not belong to the current user.

    """
    watchlist_item = get_object_or_404(WatchListItem, item_id=item_id, user_id=request.user.id)
    watchlist_item.delete()
    return redirect('item-details', id=item_id)


@login_required
def index(request):
    """
    Renders the watchlist index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'watchlist/index.html' template with the watchlist items and their associated items.

    """
    watchlist_items = WatchListItem.objects.filter(user_id=request.user.id).select_related('item')
    items = Item.objects.filter(id__in=watchlist_items.values('item_id')).prefetch_related('itemimage_set').annotate(
        is_in_watchlist=Exists(watchlist_items.filter(item_id=OuterRef('pk')))
    )
    return render(request, 'watchlist/index.html', {
        'items': items
    })
