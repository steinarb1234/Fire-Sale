from django.shortcuts import render, get_object_or_404, redirect

from item.forms.item_form import CreateItemForm
from item.models import Item, ItemImage, ItemDetails, ItemStats


# Create your views here.
def index(request):
    return render(request, 'item/index.html', context={
        'items': Item.objects.all()
    })

def get_item_by_id(request, id):
    return render(request, 'item/item_details.html', {
        'item': get_object_or_404(Item, pk=id)
    })

def create_item(request):
    if request.method == 'POST':
        form = CreateItemForm(data=request.POST)
        if form.is_valid():
            item = form.save()

            item_image = ItemImage(image=request.POST['image'], item=item)
            item_image.save()

            return redirect('item-index')
    else:
        form = CreateItemForm()
    return render(request, 'item/create_item.html', {
        'form': form
    })