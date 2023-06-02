# Import statements
from datetime import date
from django.template.loader import render_to_string
from django.db.models import Max, Avg
from django.http import JsonResponse
import django.utils.datetime_safe
from django.shortcuts import render, redirect, get_object_or_404
from item.models import ItemStats
from offer.forms.offer_form import CreateOfferForm, CreateOfferDetailsForm, PaymentForm, RatingForm
from django.contrib.auth import get_user_model
from rating.models import Rating
from user.forms.user_form import CheckOutUserUpdateForm, CheckOutProfileUpdateForm
from offer.models import Offer
from django.contrib.auth.decorators import login_required
from item.models import ItemImage,ItemStats
from user.models import User, Notification
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .service import OfferService


@login_required
def offer_details(request, offer_id):
    """
    Displays the details of a specific offer.

    Args:
        request (HttpRequest): The HTTP request object.
        offer_id (int): The ID of the offer to display.

    Returns:
        HttpResponse: If the user has permission to view the offer, renders the 'offer/offer_details.html' template
        with the offer details, including item images, highest price, and seller rating.
        
    Raises:
        PermissionDenied: If the current user does not have permission to view the offer.

    """
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
    """
    Opens a pop-up window to create a new offer for the specified item.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item for which the offer is being created.

    Returns:
        JsonResponse: A JSON response containing the rendered HTML form for creating a new offer.

    """
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
    """
    Creates a new offer for the specified item.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item for which the offer is being created.

    Returns:
        HttpResponse: If the request method is POST and the form data is valid, redirects to the 'offer-details' page
        for the created offer.
        Otherwise, renders the 'offer/create_offer.html' template with the offer creation forms.

    """
    if request.method == 'POST':
        print('posting')
        offer_form = CreateOfferForm(data=request.POST)
        offer_details_form = CreateOfferDetailsForm(data=request.POST)
        if offer_form.is_valid() and offer_details_form.is_valid():
            offer_id = OfferService.create_offer(offer_form, offer_details_form, request.user.id, item_id)
            return redirect('offer-details', offer_id)
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
    """
    Changes the status of an offer and sends notifications accordingly.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the offer to change the status.
        itemid (int): The ID of the item associated with the offer.
        button (str): The new status for the offer.

    Returns:
        HttpResponse: Redirects to the 'item-offers' page for the specified item.

    """
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
    """
    Sends a notification for a changed offer status.

    Args:
        offer (Offer): The offer for which the status has changed.

    """
    notification = Notification()
    notification.message = f'Your offer for "{offer.item}" has been {offer.status}!'
    notification.datetime = django.utils.datetime_safe.datetime.now()
    notification.href = 'offer-details'
    notification.href_parameter = offer.id
    notification.receiver = offer.buyer
    notification.save()


@login_required
def edit_offer(request, id, itemid):
    """
    Edits an existing offer.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the offer to edit.
        itemid (int): The ID of the item associated with the offer.

    Returns:
        HttpResponse: If the user has permission and the request method is POST with valid form data,
        redirects to the 'offer-details' page for the edited offer.
        Otherwise, renders the 'offer/edit_offer.html' template with the offer edit forms.

    Raises:
        PermissionDenied: If the current user does not have permission to edit the offer.

    """
    offer_to_change = get_object_or_404(Offer, pk=id)
    offer = Offer.objects.get(pk=id)
    
    if offer.buyer.id != request.user.id:
            raise PermissionDenied()
    else:
        if request.method == "POST":
            offer_form = CreateOfferForm(data=request.POST, instance=offer_to_change)
            offer_details_form = CreateOfferDetailsForm(data=request.POST, instance=offer_to_change.offerdetails)
            
            if offer_form.is_valid() and offer_details_form.is_valid():
                offer_id = OfferService.edit_offer(offer_form, offer_details_form, offer.seller)
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
    """
    Deletes an existing offer.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the offer to delete.

    Returns:
        HttpResponse: Redirects to the 'my-offers' page after deleting the offer.
        
    """
    offer_to_delete = get_object_or_404(Offer, pk=id)
    if offer_to_delete.buyer.id != request.user.id:
            raise PermissionDenied()
    offer_to_delete.delete()

    return redirect('my-offers')

@login_required
def checkout(request, offer_id):
    """
    Handles the checkout process for an offer.

    Args:
        request (HttpRequest): The HTTP request object.
        offer_id (int): The ID of the offer to checkout.

    Returns:
        HttpResponse: If the user has permission and the request method is POST with valid form data,
        redirects to the appropriate page based on the checkout process.
        Otherwise, renders the 'offer/checkout.html' template with the checkout forms.

    Raises:
        PermissionDenied: If the current user does not have permission to checkout the offer.

    """
    auth_user = get_user_model()
    offer = get_object_or_404(Offer, pk=offer_id)
    
    user_instance = get_object_or_404(User, pk=offer.buyer_id)
    user_info_instance = user_instance.userinfo
    user_profile_instance = user_info_instance.userprofile
    auth_user_instance = auth_user.objects.get(pk=offer.buyer.id)
    
    other_offers_on_item = Offer.objects.filter(item_id=offer.item_id)
    item_stats = get_object_or_404(ItemStats, pk=offer.item_id)
    

    if offer.buyer.id != request.user.id:
            raise PermissionDenied()
    else:
        if request.method == 'POST':
            user_form = CheckOutUserUpdateForm(request.POST, instance=user_instance)
            user_profile_form = CheckOutProfileUpdateForm(request.POST, instance=user_profile_instance)
            payment_form = PaymentForm(data=request.POST)
            rating_form = RatingForm(data=request.POST)
            
            if user_form.is_valid() and user_profile_form.is_valid() and payment_form.is_valid():
                
                redirect_url = OfferService.handle_checkout(user_form, user_profile_form, rating_form, request, auth_user_instance, user_info_instance, item_stats, other_offers_on_item, offer)

                return redirect(redirect_url)

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

