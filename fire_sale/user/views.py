# Import statements
from django.contrib.auth.forms import UserCreationForm
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
from django.db.models import Max

# View functions for 'user':
def register(request):
    
    if request.method == 'POST':
        user_creation_form = UserCreationForm(request.POST)
        user_info_creation_form = CustomUserCreationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_creation_form.is_valid() and user_info_creation_form.is_valid() and user_profile_form.is_valid():

            # Get user form but don't save yet
            user_form = user_creation_form.save(commit=False)

            # Update email and full_name in User model
            user_form.email = user_info_creation_form.cleaned_data['email']
            user_form.first_name = user_info_creation_form.cleaned_data['full_name']
            
            # Now save user form
            user_form.save()

            # Save custom user info form
            user_info_creation_form.instance.user_name = user_form.username
            user_info_creation_form.save()

            # Create and save UserInfo
            user_info = UserInfo()
            user_info.user_id = User.objects.get(user_name=user_form.username).id
            user_info.save()

            # Save user profile form
            # Attach user_info instance to UserProfile instance before saving
            user_profile_form.instance.user_info = user_info
            user_profile_form.save()

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
    
    auth_user = get_user_model()
    user_instance = get_object_or_404(User, pk=id)
    user_info_instance = user_instance.userinfo
    user_profile_instance = user_info_instance.userprofile
    auth_user_instance = auth_user.objects.get(pk=id)

    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=user_instance)
        user_profile_form = UserProfileUpdateForm(request.POST, instance=user_profile_instance)
        user_info_form = UserInfoUpdateForm(request.POST, instance=user_info_instance)

        if user_form.is_valid() and user_profile_form.is_valid() and user_info_form.is_valid():
            user_form.save()
            user_info_form.save()

            # Update the related auth_user instance directly
            auth_user_instance.email = user_form.cleaned_data['email']
            auth_user_instance.first_name = user_form.cleaned_data['full_name']
            auth_user_instance.username = user_form.cleaned_data['user_name']
            auth_user_instance.save()  # Save the updated auth_user instance

            user_profile = user_profile_form.save(commit=False)
            user_profile.user_info = user_info_instance
            user_profile.save()

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
    try:
        user_offers = Offer.objects.filter(buyer_id=request.user.id).prefetch_related('item')
        item_ids = user_offers.values_list('item__id', flat=True)
        highest_price = Offer.objects.filter(item__id__in=item_ids).aggregate(highest_price=Max('amount'))['highest_price']

    except ObjectDoesNotExist:
        user_offers = None
    
    return render(request, 'user/my_offers.html', {
        "user_offers": user_offers,
        "highest_price": highest_price,
    })

from django.db.models import Count
def my_listings(request):
    
    user_items = Item.objects.filter(seller=request.user.id)
    
    # Calculate highest price for each item
    highest_prices = Offer.objects.filter(item__in=user_items).values('item_id').annotate(highest_price=Max('amount'))
    highest_prices_dict = {item['item_id']: item['highest_price'] for item in highest_prices}
    
    # Fetch item stats
    item_stats = ItemStats.objects.prefetch_related('item', 'item__offer_set', 'status').filter(item__seller_id=request.user.id)
    for item_stat in item_stats:
        item_stat.highest_price = highest_prices_dict.get(item_stat.item.id, 'No offer')
        
        # Calculate number of watchers for each item
        item_stat.watchers = WatchListItem.objects.filter(item=item_stat).count()
    
    return render(request, 'user/my_listings.html', context={
        'item_stats': item_stats,
    })


def notifications(request):
    notifications = Notification.objects.filter(receiver=request.user.id)
    for notification in notifications:
        if notification.href_parameter:
            notification.href = resolve_url(notification.href, notification.href_parameter)
        else:
            notification.href = resolve_url(notification.href)

    return render(request, 'user/notifications.html', context={
        'notifications': notifications
    })
