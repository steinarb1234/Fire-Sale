from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from user.forms.user_form import CustomUserCreationForm, UserProfileForm
from user.models import UserProfile, User, UserInfo

# Bæta við öllum upplýsingum...
def register(request):
    if request.method == 'POST':
        
        user_creation_form = UserCreationForm(request.POST)
        user_info_creation_form = CustomUserCreationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_creation_form.is_valid() and user_info_creation_form.is_valid() and user_profile_form.is_valid():
            
            # Save user form
            user_form = user_creation_form.save()
            
            # Save custom user info form
            user_info_creation_form.instance.user_name = user_form.username
            custom_user_form = user_info_creation_form.save()
            
            # Create and save UserInfo
            user_info = UserInfo()
            user_info.user_id = User.objects.get(user_name = user_form.username).id
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


def profile(request):
    return render(request, 'user/profile.html', {
        "user_instance": User.objects.get(user_name = request.user)
    })
 
def my_offers(request):
    return render(request, 'my_offers/my_offers.html')