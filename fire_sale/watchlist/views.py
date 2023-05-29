#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import WatchListItem
from .forms.watchlist_form import WatchListCreationForm
from item.models import Item

#@login_required
# Fillir whatclist út frá database

from django.shortcuts import redirect, reverse

from django.shortcuts import redirect, reverse


def add_to_watchlist(request, itemid):

    if request.method == 'POST':
        print('posting')
        watchlist_form = WatchListCreationForm()
        watchlist = watchlist_form.save(commit=False)
        watchlist.item_id = itemid
        watchlist.user_id = request.user.id
        watchlist.save()
        return redirect('item-details', id=itemid)

    return redirect('item-details', id=itemid)


def index(request):
    watchlist = WatchListItem.objects.filter(user=request.user.id)
    item_ids = watchlist.values_list('item_id', flat=True)
    items = Item.objects.filter(id__in=item_ids)
    return render(request, 'watchlist/index.html', {
        'items': items
    })
