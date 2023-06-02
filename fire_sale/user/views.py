# Import statements
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from django.core.exceptions import ObjectDoesNotExist
from item.models import Item, ItemStats, ItemDetails
from watchlist.models import WatchListItem
from offer.models import Offer
from rating.models import Rating
from user.forms.user_form import CustomUserCreationForm, UserProfileForm, CustomUserUpdateForm, UserProfileUpdateForm, UserInfoUpdateForm
from user.models import UserProfile, User, UserInfo, Notification
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Count
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .service import UserService


def register(request):
    """
    Handles the registration of a new user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: If the request method is POST and the form data is valid, redirects to the 'login' page.
        Otherwise, renders the 'user/register.html' template with the registration forms.
    """
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        user_info_creation_form = CustomUserCreationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)

        if user_creation_form.is_valid() and user_info_creation_form.is_valid() and user_profile_form.is_valid():
            UserService.create_user(user_creation_form, user_info_creation_form, user_profile_form)
            return redirect('login')
    else:
        user_creation_form = UserCreationForm()
        user_info_creation_form = CustomUserCreationForm()
        user_profile_form = UserProfileForm()

    return render(request, 'user/register.html', 
                  {'user_creation_form': user_creation_form, 
                   'user_info_creation_form': user_info_creation_form, 
                   'user_profile_form': user_profile_form})

@login_required
def update_profile(request, id):
    """
    Updates the profile information of the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the user to update.

    Returns:
        HttpResponse: If the user is not authorized to update the profile, raises PermissionDenied.
        If the request method is POST and the form data is valid, redirects to the 'user-profile' page.
        Otherwise, renders the 'user/update_user.html' template with the profile update forms.

    """
    auth_user = get_user_model()
    user_instance = get_object_or_404(User, pk=id)
    user_info_instance = user_instance.userinfo
    user_profile_instance = user_info_instance.userprofile
    auth_user_instance = auth_user.objects.get(pk=id)

    if user_instance.id != request.user.id:
        raise PermissionDenied()
    else:
        if request.method == 'POST':
            user_form = CustomUserUpdateForm(request.POST, instance=user_instance)
            user_profile_form = UserProfileUpdateForm(request.POST, instance=user_profile_instance)
            user_info_form = UserInfoUpdateForm(request.POST, instance=user_info_instance)

            if user_form.is_valid() and user_profile_form.is_valid() and user_info_form.is_valid():
                UserService.save_user_info(user_form, user_info_form, user_profile_form, auth_user_instance, user_info_instance)
                return redirect('user-profile')
        else:
            user_form = CustomUserUpdateForm(instance=user_instance)
            user_profile_form = UserProfileUpdateForm(instance=user_profile_instance)
            user_info_form = UserInfoUpdateForm(instance=user_info_instance)

        return render(request, 'user/update_user.html', {
            'user_form': user_form,
            'user_profile_form': user_profile_form,
            'user_info_form': user_info_form,
            'id': id
    })

@login_required
def user_profile(request):
    """
    Displays the profile information of the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'user/profile.html' template with the user's profile information,
        including the user instance, user info, user profile, and user ratings.

    """
    user_instance = User.objects.get(id = request.user.id)
    user_info = UserInfo.objects.get(user=user_instance)
    user_profile = UserProfile.objects.get(user_info=user_info)
    user_ratings = Rating.objects.filter(offer__seller_id=request.user.id)


    return render(request, 'user/profile.html', {
        "user_instance": user_instance,
        "user_info": user_info,
        "user_profile": user_profile,
        "user_ratings": user_ratings,
    })


@login_required
def my_offers(request):
    """
    Displays the offers made by the authenticated user for items.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'user/my_offers.html' template with the user's offers for items and the highest price among them.

    Raises:
        ObjectDoesNotExist: If no offers exist for the user.

    """
    try:
        user_offers = Offer.objects.filter(buyer_id=request.user.id).prefetch_related('item', 'offerdetails', 'item__offer_set', 'item__itemstats', 'item__itemstats__status')
        item_ids = user_offers.values_list('item__id', flat=True)
        highest_price = Offer.objects.filter(item__id__in=item_ids).aggregate(highest_price=Max('amount'))['highest_price']

    except ObjectDoesNotExist:
        user_offers = None
    
    return render(request, 'user/my_offers.html', {
        "user_offers": user_offers,
        "highest_price": highest_price,
    })

@login_required
def my_listings(request):
    """
    Displays the listings created by the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'user/my_listings.html' template with the user's listings,
        including the highest price for each item, the count of watchers, and item statistics.

    """
    # Calculate highest price for each item
    user_items = Item.objects.filter(seller=request.user.id)
    highest_prices = Offer.objects.filter(item__in=user_items).values('item_id').annotate(highest_price=Max('amount'))
    highest_prices_dict = {item['item_id']: item['highest_price'] for item in highest_prices}

    # Get wathclist
    watchlist = WatchListItem.objects.filter(item__item_id__in=user_items).annotate(count=Count('item_id')).values('item_id', 'count')
    item_watchers = list(watchlist.annotate(Count('item_id')).values('item_id', 'count'))
    item_watchers_dict = {item['item_id']: item['count'] for item in item_watchers}
    
    # Fetch item stats
    item_stats = ItemStats.objects.prefetch_related('item', 'item__offer_set', 'status').filter(item__seller_id=request.user.id)

    for item_stat in item_stats:
        item_stat.highest_price = highest_prices_dict.get(item_stat.item.id, 'No offer')
        item_stat.watchers = item_watchers_dict.get(item_stat.item.id, 0)
    
    return render(request, 'user/my_listings.html', context={
        'item_stats': item_stats,
    })

@login_required
def notifications(request):
    """
    Displays the notifications for the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'user/notifications.html' template with the user's notifications,
        sorted by datetime.

    """
    notifications = Notification.objects.filter(receiver=request.user.id).order_by('datetime')
    for notification in notifications:
        if notification.href_parameter:
            notification.href = resolve_url(notification.href, notification.href_parameter)
        else:
            notification.href = resolve_url(notification.href)

    return render(request, 'user/notifications.html', context={
        'all_notifications': notifications
    })

@login_required
def mark_notification_as_seen(request, notification_id):
    """
    Marks a notification as seen for the authenticated user.

    Args:
        request (HttpRequest): The HTTP request object.
        notification_id (int): The ID of the notification to mark as seen.

    Returns:
        JsonResponse: Returns a JSON response with the marked notification.

    """
    notification = Notification.objects.get(pk=notification_id)
    notification.seen = True
    notification.save()
    return JsonResponse({'notification': str(notification)})


