from datetime import date

import django
from user.models import Notification
from item.models import Item
from rating.models import Rating
from offer.forms.offer_form import RatingForm
from item.models import Item, ItemStatuses

class OfferService:
    
    @staticmethod
    def create_offer(offer_form, offer_details_form, buyer_id, item_id):
        """
        Creates a new offer for an item.

        Args:
            offer_form (OfferForm): The form instance containing the offer data.
            offer_details_form (OfferDetailsForm): The form instance containing the offer details data.
            buyer_id (int): The ID of the buyer making the offer.
            item_id (int): The ID of the item for which the offer is being made.

        Returns:
            int: The ID of the created offer.

        """
        print('Create offer')
        # Save the offer.
        offer = offer_form.save(commit=False)
        offer.buyer_id = buyer_id
        offer.item_id = item_id
        offer.seller_id = Item.objects.get(pk=item_id).seller_id
        offer.save()

        # Save the offer details.
        offer_details = offer_details_form.save(commit=False)
        offer_details.offer_id = offer.id
        offer_details.start_date = date.today()
        offer_details.save()

        # Create the notification for the seller.
        notification_to_seller = Notification()
        notification_to_seller.message = f'Your item "{offer.item}" has received an offer of ${offer.amount}!'
        notification_to_seller.href = 'offer-details'
        notification_to_seller.href_parameter = offer.id
        notification_to_seller.receiver = offer.seller
        notification_to_seller.save()
        
        return offer.id
    
    @staticmethod
    def edit_offer(offer_form, offer_details_form, seller):
        # Save the offer.
        offer = offer_form.save(commit=False)
        offer_details = offer_details_form.save(commit=False)
        offer_details.offer = offer
        offer.save()
        offer_details.save()

        # Create the notification for the seller.
        notification_to_seller = Notification()
        notification_to_seller.message = f'An offer for your listing: "{offer.item}" has been edited'
        notification_to_seller.datetime = django.utils.datetime_safe.datetime.now()
        notification_to_seller.href = 'offer-details'
        notification_to_seller.href_parameter = offer.id
        notification_to_seller.receiver = seller
        notification_to_seller.save()

        return offer.id
    
    def handle_checkout(user_form, user_profile_form, rating_form, request, auth_user_instance, user_info_instance, item_stats, other_offers_on_item, offer):
        user_form.save()
        user_profile_form.save()
        
        if rating_form.is_valid():
            # If the form is valid, save the instance
            rating_instance = rating_form.save(commit=False)
            rating_instance.offer = offer
            try:
                existing_rating = Rating.objects.get(offer=offer)
            except Rating.DoesNotExist:
                rating_instance.save()
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

        other_offers_on_item.update(status="Rejected")

        offer.status = "Item purchased"
        offer.save()

        notification_to_seller = Notification()
        notification_to_seller.message = f'Your listing: "{offer.item}" has been purchased!'
        notification_to_seller.datetime = django.utils.datetime_safe.datetime.now()
        notification_to_seller.href = 'offer-details'
        notification_to_seller.href_parameter = offer.id
        notification_to_seller.receiver = offer.seller
        notification_to_seller.save()

        return 'item-index'