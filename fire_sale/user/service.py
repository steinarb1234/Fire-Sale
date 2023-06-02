from user.models import User, UserInfo
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


class UserService:
    
    @staticmethod
    def create_user(user_creation_form, user_info_creation_form, user_profile_form):
        print('Service')
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

        categories_dicts = list(Category.objects.values('name'))
        categories = [category['name'] for category in categories_dicts]
        print(categories)
        for name in categories:
            category_views = CategoryViews()
            category_views.category_views = 0
            category_views.category_id = name
            category_views.user_id = user_info.user_id
            category_views.save()

        return user_form
    
    @staticmethod
    def save_user_info(user_form, user_info_form, user_profile_form, auth_user_instance, user_info_instance):
        user_form.save()
        user_info_form.save()

        # Update the related auth_user instance directly
        auth_user_instance.email = user_form.cleaned_data['email']
        auth_user_instance.first_name = user_form.cleaned_data['full_name']
        auth_user_instance.username = user_form.cleaned_data['user_name']
        auth_user_instance.save()  # Save the updated auth_user instance

        # Save the UserProfile form
        user_profile = user_profile_form.save(commit=False)
        user_profile.user_info = user_info_instance
        user_profile.save()
    