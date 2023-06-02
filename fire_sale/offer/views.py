from datetime import date
from django.template.loader import render_to_string
from django.db.models import Sum, Max, Avg
from django.http import JsonResponse
import django.utils.datetime_safe
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item, ItemStats, ItemStatuses
from offer.forms.offer_form import ContactInformationForm, CreateOfferForm, CreateOfferDetailsForm, PaymentForm, \
    RatingForm
from django.contrib.auth import get_user_model

from rating.models import Rating
from user.forms.user_form import CheckOutUserUpdateForm, CheckOutProfileUpdateForm

from offer.models import Offer, OfferDetails
from django.contrib.auth.decorators import login_required
from item.models import Item, ItemImage, ItemDetails, ItemStats
from user.models import User, UserProfile, Notification
from django.http import HttpRequest
from django.shortcuts import render
from django.core.exceptions import PermissionDenied



@login_required
def offer_details(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)

    if offer.buyer.id != request.user.id and offer.seller.id != request.user.id:
            raise PermissionDenied()
    else:
        item_images = ItemImage.objects.filter(item=offer.item)
        highest_price = Offer.objects.filter(item_id=offer.item_id).aggregate(Max('amount'))['amount__max'] or '(No offers)'
        try:
            seller_rating = round(Rating.objects.filter(offer_id__seller=offer.seller).aggregate(Avg('rating'))['rating__avg'], 1)
        except TypeError:
            seller_rating = 'No rating'
        return render(request, 'offer/offer_details.html', {
            "offer": offer,
            'item_images': item_images,
            'highest_price': highest_price,
            'seller_rating': seller_rating,
    })


@login_required
def open_offer_window(request, item_id):
    print(item_id)
    print("ajax")
    offer_form = CreateOfferForm()
    offer_details_form = CreateOfferDetailsForm()
    html_form = render_to_string('offer/create_offer.html', {
        'offer_form': offer_form,
        'offer_details_form': offer_details_form,
        'item_id': item_id
    }, request=request)
    return JsonResponse({'html_form': html_form})
    

@login_required
def create_offer(request, item_id):
        
    if request.method == 'POST':
        print('posting')
        offer_form = CreateOfferForm(data=request.POST)
        offer_details_form = CreateOfferDetailsForm(data=request.POST)
        if offer_form.is_valid() and offer_details_form.is_valid():
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
        changed_offer_send_notification(offer)

        if offer.status == 'Accepted':
            other_offers = Offer.objects.filter(item_id=offer.item_id).exclude(id=offer.id)
            for other_offer in other_offers:
                other_offer.status = "Rejected"
                changed_offer_send_notification(other_offer)
                other_offer.save()
    return redirect('item-offers', item_id=itemid)


def changed_offer_send_notification(offer):
    notification = Notification()
    notification.message = f'Your offer for "{offer.item}" has been {offer.status}!'
    notification.datetime = django.utils.datetime_safe.datetime.now()
    notification.href = 'offer-details'
    notification.href_parameter = offer.id
    notification.receiver = offer.buyer
    notification.save()


@login_required
def edit_offer(request, id, itemid):
    offer_to_change = get_object_or_404(Offer, pk=id)

    offer = Offer.objects.get(pk=id)
    if offer.buyer.id != request.user.id:
            raise PermissionDenied()
    else:
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

@login_required
def delete_offer(request, id):
    offer_to_delete = get_object_or_404(Offer, pk=id)
    offer_to_delete.delete()

    return redirect('my-offers')

@login_required
def checkout(request, offer_id):
    
    # Reyndi að fá vistuðu uplýsingarnar, veit ekki afh það virkar ekki - Steinar
    auth_user = get_user_model()
    offer = get_object_or_404(Offer, pk=offer_id)
    print(offer.buyer_id)
    
    user_instance = get_object_or_404(User, pk=offer.buyer_id)
    print(user_instance)
    
    user_info_instance = user_instance.userinfo
    user_profile_instance = user_info_instance.userprofile
    auth_user_instance = auth_user.objects.get(pk=offer.buyer.id)
    
    other_offers_on_item = Offer.objects.filter(item_id=offer.item_id)
    item_stats = get_object_or_404(ItemStats, pk=offer.item_id)
    
    if request.method == 'POST':
        user_form = CheckOutUserUpdateForm(request.POST, instance=user_instance)
        user_profile_form = CheckOutProfileUpdateForm(request.POST, instance=user_profile_instance)
        payment_form = PaymentForm(data=request.POST)
        rating_form = RatingForm(data=request.POST)
        
        if user_form.is_valid() and user_profile_form.is_valid() and payment_form.is_valid():
            
        
            # Save user profile information and rating
            user_form.save()
            user_profile_form.save()
            
            if rating_form.is_valid():
                # If the form is valid, save the instance
                rating_instance = rating_form.save(commit=False)
                rating_instance.offer = offer
                try:
                    existing_rating = Rating.objects.get(offer=offer)
                except Rating.DoesNotExist:
                    pass
                else:
                    rating_form = RatingForm(request.POST, instance=existing_rating)
                    rating_instance.save()
                                
                # Update the related auth_user instance directly
                auth_user_instance.email = user_form.cleaned_data['email']
                auth_user_instance.first_name = user_form.cleaned_data['full_name']
                auth_user_instance.save()  
                
                user_profile = user_profile_form.save(commit=False)
                user_profile.user_info = user_info_instance
                user_profile.save()

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

                return redirect('item-index')
    else:
        user_form = CheckOutUserUpdateForm(instance=user_instance)
        user_profile_form = CheckOutProfileUpdateForm(instance=user_profile_instance)
        payment_form = PaymentForm()
        rating_form = RatingForm()
    
    return render(request, 'offer/checkout.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
        'payment_form': payment_form,
        'rating_form': rating_form,
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