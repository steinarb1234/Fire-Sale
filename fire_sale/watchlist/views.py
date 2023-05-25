from django.shortcuts import render
from .models import WatchListItem
from item.models import Item

def index(request):
    watchlist = WatchListItem.objects.filter(user=request.user.id)
    item_ids = watchlist.values_list('item_id', flat=True)
    items = Item.objects.filter(id__in=item_ids)
    return render(request, 'watchlist/index.html', {
        'items': items
    })
