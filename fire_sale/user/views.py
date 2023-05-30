from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect, resolve_url
from django.core.exceptions import ObjectDoesNotExist
from item.models import Item
from offer.models import Offer, OfferDetails
from user.forms.user_form import CustomUserCreationForm, UserProfileForm, CustomUserUpdateForm, UserProfileUpdateForm, UserInfoUpdateForm
from user.models import UserProfile, User, UserInfo, Notifications
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Max

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
    print(user_instance)
    print(user_info)
    print(user_profile)
    return render(request, 'user/profile.html', {
        "user_instance": user_instance,
        "user_info": user_info,
        "user_profile": user_profile,
    })


@login_required
def my_offers(request):
    try:
        user_offers = Offer.objects.filter(buyer_id=request.user.id)
        item_ids = user_offers.values_list('item__id', flat=True)
        highest_price = Offer.objects.filter(item__id__in=item_ids).aggregate(highest_price=Max('amount'))['highest_price']

    except ObjectDoesNotExist:
        user_offers = None
    
    return render(request, 'user/my_offers.html', {
        "user_offers": user_offers,
        "highest_price": highest_price
    })



def my_listings(request):
    # Get all items where the current user is the seller
    user_items = Item.objects.filter(seller=request.user.id)

    # Get the highest price per item
    highest_prices = Offer.objects.filter(item__in=user_items).values('item_id').annotate(highest_price=Max('amount'))

    highest_prices_dict = {item['item_id']: item['highest_price'] for item in highest_prices}

    return render(request, 'user/my_listings.html', context={
        'item_stats': user_items,
        "highest_prices_dict": highest_prices_dict,
    })



def notifications(request):
    notifications = Notifications.objects.filter(receiver=request.user.id)
    for notification in notifications:
        notification.href = resolve_url(notification.href)

    return render(request, 'user/notifications.html', context={
        'notifications': notifications
    })
