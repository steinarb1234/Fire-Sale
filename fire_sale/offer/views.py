from django.shortcuts import render, redirect

from offer.forms.offer_form import CheckoutForm, CreateOfferForm
from offer.models import Offer, OfferDetails


# Create your views here.

def index(request):
    return render(request, 'offer/index.html', context={
        'offer': Offer.objects.all()
    })


def create_offer(request):
    if request.method == 'POST':
        form = CreateOfferForm(data=request.POST)
        if form.is_valid():
            # Save items in inherited model
            offer = form.save()

            item_details = OfferDetails(
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                message=request.POST['message'],
                offer=offer
            )
            item_details.save()

            return redirect('item-details', offer.item_id)
    else:
        form = CreateOfferForm()
    return render(request, 'offer/create_offer.html', {
        'form': form
    })


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            #
            # item_image = ItemImage(image=request.POST['image'], item=item)
            # item_image.save()

            return redirect('user-profile')
    else:
        form = CheckoutForm()
    return render(request, 'offer/checkout.html', {
        'form': form
    })