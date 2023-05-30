from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item, ItemStats, ItemStatuses
from offer.forms.offer_form import ContactInformationForm, CreateOfferForm, CreateOfferDetailsForm, PaymentForm, \
    RatingForm
from offer.models import Offer, OfferDetails
from django.contrib.auth.decorators import login_required

from user.models import User, UserProfile


# Create your views here.

def offer_details(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    return render(request, 'offer/offer_details.html', {
        "offer": offer,
    })

@login_required
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
    
@login_required
def change_offer_status(request, id, itemid, button):
    if request.method == 'POST':
        offer_to_change = Offer.objects.get(pk=id)
        offer_to_change.status = button
        offer_to_change.save()
        return redirect('item-offers', item_id=itemid)

    return redirect('item-offers', item_id=itemid)
    

@login_required
def checkout(request, offer_id):
    # Að reyna að fá vistuðu uplýsingarnar, veit ekki afh það virkar ekki - Steinar
    offer = get_object_or_404(Offer, pk=offer_id)
    other_offers_on_item = Offer.objects.filter(item_id=offer.item_id)
    item_stats = get_object_or_404(ItemStats, pk=offer.item_id)
    user_profile = get_object_or_404(UserProfile, pk=offer.buyer_id)

    if request.method == 'POST':
        contact_information_form = ContactInformationForm(data=request.POST, instance=user_profile)
        payment_form = PaymentForm(data=request.POST)
        if contact_information_form.is_valid() and payment_form.is_valid():
            contact_information = contact_information_form
            payment = payment_form

            item_stats.status = ItemStatuses(status="Sold")
            item_stats.save()

            other_offers_on_item.status = "Rejected"
            for other_offer in other_offers_on_item:
                other_offer.save()

            offer.status = "Item purchased"
            offer.save()

            return redirect('review', offer_id)
    else:
        contact_information_form = ContactInformationForm(instance=user_profile)
        payment_form = PaymentForm()
        rating_form = RatingForm()
    return render(request, 'offer/checkout.html', {
        'contact_information_form': contact_information_form,
        'payment_form': payment_form,
        'offer_id': offer_id,
    })


@login_required
def payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(data=request.POST)
        if payment_form.is_valid():
            payment = payment_form

            return redirect('user-profile')
    else:
        payment_form = PaymentForm()
    return render(request, 'offer/payment.html', {
        'payment_form': payment_form,
    })


@login_required
def review(request, offer_id):
    if request.method == 'POST':
        rating_form = RatingForm(data=request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.offer_id = offer_id
            rating.save()

            return redirect('user-profile')
    else:
        rating_form = RatingForm()
    return render(request, 'offer/review.html', {
        'rating_form': rating_form,
        'offer_id': offer_id,
    })