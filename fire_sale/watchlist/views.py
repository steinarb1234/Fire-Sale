from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import WatchListItem
from .forms.watchlist_form import WatchListCreationForm
from item.models import Item

#@login_required
# Fillir whatclist út frá database

def add_to_watchlist(request, itemid):
    if request.method == 'POST':
        item_id = request.POST.get('itemid')  # Retrieve the item ID from the form data
        watchlist_form = WatchListCreationForm(request.POST)
        if watchlist_form.is_valid():
            watchlist = watchlist_form.save(commit=False)
            watchlist.item_id = item_id
            watchlist.user_id = request.user.id
            print(watchlist.item_id, watchlist.user_id)
            watchlist.save()
            # Add any additional logic or redirection after saving to the database
            return redirect(request.path)  # Replace 'some_view' with the desired URL
    else:
        watchlist_form = WatchListCreationForm()
    
    context = {'watchlist_form': watchlist_form,
               'itemid': itemid}
    return render(request, 'item/item_details.html', context)
            
def index(request):
    watchlist = WatchListItem.objects.filter(user=request.user.id)
    item_ids = watchlist.values_list('item_id', flat=True)
    items = Item.objects.filter(id__in=item_ids)
    return render(request, 'watchlist/index.html', {
        'items': items
    })
