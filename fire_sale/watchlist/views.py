from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import WatchListItem
from .forms.watchlist_form import WatchListCreationForm
from item.models import Item

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
    watchlist = WatchListItem.objects.filter(user=request.user.id)
    item_ids = watchlist.values_list('item_id', flat=True)
    items = Item.objects.filter(id__in=item_ids)
    return render(request, 'watchlist/index.html', {
        'items': items
    })
