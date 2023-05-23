from django.shortcuts import render, redirect

from offer.forms.offer_form import CheckoutForm
from offer.models import Offer


# Create your views here.

def index(request):
    return render(request, 'offer/index.html', context={
        'offer': Offer.objects.all()
    })

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            #
            # item_image = ItemImage(image=request.POST['image'], item=item)
            # item_image.save()

            return redirect('item-index')
    else:
        form = CheckoutForm()
    return render(request, 'offer/checkout.html', {
        'form': form
    })