from datetime import date

from django.shortcuts import render, redirect

from item.models import Item
from offer.forms.offer_form import CheckoutForm, CreateOfferForm, CreateOfferDetailsForm
from offer.models import Offer, OfferDetails


# Create your views here.

def offer_details(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    return render(request, 'offer/offer_details.html', {
        "offer": offer,
    })


def create_offer(request, item_id):
    if request.method == 'POST':
        offer_form = CreateOfferForm(data=request.POST)
        offer_details_form = CreateOfferDetailsForm(data=request.POST)
        if offer_form.is_valid() and offer_details_form.is_valid():
            # Save items in inherited model
            offer = offer_form.save(commit=False)
            offer.buyer_id = request.user.id
            offer.item_id = item_id
            offer.seller_id = Item.objects.get(pk=item_id).seller_id
            offer.save()

            offer_details = offer_details_form.save(commit=False)
            offer_details.offer_id = offer.id
            offer_details.start_date = date.today()
            offer_details.save()

            return redirect('item-index')
    else:
        offer_form = CreateOfferForm()
        offer_details_form = CreateOfferDetailsForm()
    return render(request, 'offer/create_offer.html', {
        'offer_form': offer_form,
        'offer_details_form': offer_details_form,
        'item_id': item_id
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