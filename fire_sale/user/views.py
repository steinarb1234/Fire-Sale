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
            user_form = user_creation_form.save()
            user_info_creation_form.instance.user = user_form
            user_info_creation_form.save()

            # print('User: ' + user_info_creation_form.instance.user.id)
            user_info = UserInfo(user=user_form.u)
            user_info.user = request.user.id
            user_info.save()
            
            return redirect('login')
    else:
        user_creation_form = UserCreationForm()
        user_info_creation_form = CustomUserCreationForm()
    
    return render(request, 'user/register.html', {'user_creation_form': user_creation_form, 'user_info_creation_form': user_info_creation_form})

def profile(request):
    return render(request, 'user/profile.html')
 
