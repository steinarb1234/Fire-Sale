from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchListItem
from .forms.watchlist_form import WatchListCreationForm
from item.models import Item
from django.db.models import Exists, OuterRef


@login_required
def add_to_watchlist(request, item_id):

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
    watchlist_item = get_object_or_404(WatchListItem, item_id=item_id, user_id=request.user.id)
    watchlist_item.delete()
    return redirect('item-details', id=item_id)


@login_required
def index(request):
    watchlist_items = WatchListItem.objects.filter(user_id=request.user.id)
    items = Item.objects.filter(id__in=watchlist_items.values('item_id')).annotate(
        is_in_watchlist=Exists(watchlist_items.filter(item_id=OuterRef('pk')))
    )
    return render(request, 'watchlist/index.html', {
        'items': items
    })
