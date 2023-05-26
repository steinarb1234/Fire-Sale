from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from user.forms.user_form import CustomUserCreationForm, UserProfileForm
from user.models import UserProfile, User, UserInfo


def register(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = CustomUserCreationForm(request.POST, initial={'user_name': form1['username'].value()})
        if form1.is_valid() and form2.is_valid():
            
            user = form1.save()
            form2 = CustomUserCreationForm(request.POST, initial={'user_name': user.username})
            form2.instance.user_name = user.username
            form2.save()
            
            return redirect('login')
    else:
        form1 = UserCreationForm()
        form2 = CustomUserCreationForm()
    
    return render(request, 'user/register.html', {'form1': form1, 'form2': form2})

def profile(request):
    return render(request, 'user/profile.html')
 
