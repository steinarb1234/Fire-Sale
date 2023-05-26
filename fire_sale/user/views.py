from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from user.forms.user_form import CustomUserCreationForm, UserProfileForm
from user.models import UserProfile, User, UserInfo


def register(request):
    if request.method == 'POST':
        
        user_creation_form = UserCreationForm(request.POST)
        user_info_creation_form = CustomUserCreationForm(request.POST)
        
        if user_creation_form.is_valid() and user_info_creation_form.is_valid():
            
            # Fill in first form
            user_form = user_creation_form.save()
            
            # Fill in second form
            user_info_creation_form.instance.user_name = user_form.username
            user_info_creation_form.save()

            # Want to fill the UserInfo() module with nothing, but make the id from the first form saved
            user_info = UserInfo()
            user_info.user_id = User.objects.get(user_name = user_form.username).id
            user_info.save()
            
            return redirect('login')
    else:
        user_creation_form = UserCreationForm()
        user_info_creation_form = CustomUserCreationForm()
    
    return render(request, 'user/register.html', {'user_creation_form': user_creation_form, 'user_info_creation_form': user_info_creation_form})

def profile(request):
    return render(request, 'user/profile.html')
 
