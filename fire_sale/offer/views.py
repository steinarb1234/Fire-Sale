from datetime import date
from django.db.models import Sum, Max
import django.utils.datetime_safe
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item, ItemStats, ItemStatuses
from offer.forms.offer_form import ContactInformationForm, CreateOfferForm, CreateOfferDetailsForm, PaymentForm, \
    RatingForm
from offer.models import Offer, OfferDetails
from django.contrib.auth.decorators import login_required
from item.models import Item, ItemImage, ItemDetails, ItemStats
from user.models import User, UserProfile, Notification


# Create your views here.

def offer_details(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    item_images = ItemImage.objects.filter(item=offer.item)
    highest_price = Offer.objects.filter(item_id=offer_id).aggregate(Max('amount'))['amount__max'] or 0
    return render(request, 'offer/offer_details.html', {
        "offer": offer,
        'item_images': item_images,
        'highest_price': highest_price
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

            notification_to_seller = Notification()
            notification_to_seller.message = f'Your item "{offer.item}" has received an offer of ${offer.amount}!'
            notification_to_seller.datetime = django.utils.datetime_safe.datetime.now()
            notification_to_seller.href = 'offer-details'
            notification_to_seller.href_parameter = offer.id
            notification_to_seller.receiver = offer.seller
            notification_to_seller.save()

            return redirect('offer-details', offer.id)
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
        offer = Offer.objects.get(pk=id)
        offer.status = button
        offer.save()

        notification_to_buyer = Notification()
        notification_to_buyer.message = f'Your offer for "{offer.item}" has been {offer.status}!'
        notification_to_buyer.datetime = django.utils.datetime_safe.datetime.now()
        notification_to_buyer.href = 'offer-details'
        notification_to_buyer.href_parameter = offer.id
        notification_to_buyer.receiver = offer.buyer
        notification_to_buyer.save()

        return redirect('item-offers', item_id=itemid)

    return redirect('item-offers', item_id=itemid)

def edit_offer(request, id, itemid):
    offer_to_change = get_object_or_404(Offer, pk=id)

    if request.method == "POST":
        offer_form = CreateOfferForm(data=request.POST, instance=offer_to_change)
        offer_details_form = CreateOfferDetailsForm(data=request.POST, instance=offer_to_change.offerdetails)
        
        if offer_form.is_valid() and offer_details_form.is_valid():
            offer = offer_form.save(commit=False)
            offer_details = offer_details_form.save(commit=False)
            offer_details.offer = offer
            offer.save()
            offer_details.save()

            notification_to_seller = Notification()
            notification_to_seller.message = f'An offer for your listing: "{offer.item}" has been edited'
            notification_to_seller.datetime = django.utils.datetime_safe.datetime.now()
            notification_to_seller.href = 'offer-details'
            notification_to_seller.href_parameter = offer.id
            notification_to_seller.receiver = offer.seller
            notification_to_seller.save()


            return redirect('offer-details', offer_id=id)
    else:
        offer_form = CreateOfferForm(instance=offer_to_change)
        offer_details_form = CreateOfferDetailsForm(instance=offer_to_change.offerdetails)

    return render(request, 'offer/edit_offer.html', {
        'offer_form': offer_form,
        'offer_details_form': offer_details_form,
        'offer_to_change': offer_to_change,
        'id': id,
        'item_id': itemid
    })

def delete_offer(request, id):
    offer_to_delete = get_object_or_404(Offer, pk=id)
    offer_to_delete.delete()

    return redirect('my-offers')

@login_required
def checkout(request, offer_id):
    # Reyndi að fá vistuðu uplýsingarnar, veit ekki afh það virkar ekki - Steinar
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

            notification_to_seller = Notification()
            notification_to_seller.message = f'Your listing: "{offer.item}" has been purchased!'
            notification_to_seller.datetime = django.utils.datetime_safe.datetime.now()
            notification_to_seller.href = 'offer-details'
            notification_to_seller.href_parameter = offer.id
            notification_to_seller.receiver = offer.seller
            notification_to_seller.save()

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

            offer = get_object_or_404(Offer, pk=offer_id)
            notification_to_seller = Notification()
            notification_to_seller.message = f'You have received a rating for "{offer}"!'
            notification_to_seller.datetime = django.utils.datetime_safe.datetime.now()
            notification_to_seller.href = 'offer-details'   # Breyta í rating síðuna! - Steinar
            notification_to_seller.href_parameter = offer.id
            notification_to_seller.receiver = offer.seller
            notification_to_seller.save()

            return redirect('user-profile')
    else:
        rating_form = RatingForm()
    return render(request, 'offer/review.html', {
        'rating_form': rating_form,
        'offer_id': offer_id,
    })