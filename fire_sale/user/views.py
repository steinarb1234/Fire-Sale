from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django import forms
from user.forms.user_form import CustomUserCreationForm, UserProfileForm, CustomUserUpdateForm, UserProfileUpdateForm, UserInfoUpdateForm
from user.models import UserProfile, User, UserInfo

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




# def user_profile(request):
#     user_instance = User.objects.get(user_name=request.user.username)


def updateProfile(request, username):

    user_instance = get_object_or_404(User, user_name=username)
    user_info_instance = user_instance.userinfo
    user_profile_instance = user_info_instance.userprofile

    if request.method == 'POST':
        user_form = CustomUserUpdateForm(request.POST, instance=user_instance)
        user_profile_form = UserProfileUpdateForm(request.POST, instance=user_profile_instance)
        user_info_form = UserInfoUpdateForm(request.POST, instance=user_info_instance)  # New form instance
        
        if user_form.is_valid() and user_profile_form.is_valid() and user_info_form.is_valid():  # Validate new form
            user_form.save()
            user_info_form.save()  # Save UserInfo form
            user_profile = user_profile_form.save(commit=False)
            user_profile.user_info = user_info_instance
            user_profile.save()
            return redirect('user-profile')  # Replace with your correct redirection view
    else:
        user_form = CustomUserUpdateForm(instance=user_instance)
        user_profile_form = UserProfileUpdateForm(instance=user_profile_instance)
        user_info_form = UserInfoUpdateForm(instance=user_info_instance)  # New form instance

    return render(request, 'user/update_user.html', {
        'user_form': user_form,
        'user_profile_form': user_profile_form,
        'user_info_form': user_info_form,  # Include the new form in context
        'username': username
    })



def user_profile(request):
    user_instance = User.objects.get(user_name = request.user.username)
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


def my_offers(request):
    return render(request, 'my_offers/my_offers.html')
