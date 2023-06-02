# Import statements
from user.models import User, UserInfo

class UserService:
    
    @staticmethod
    def create_user(user_creation_form, user_info_creation_form, user_profile_form):
        """
        Creates a new user with the provided registration forms.

        Args:
            user_creation_form (Form): The form containing user creation data.
            user_info_creation_form (Form): The form containing user information data.
            user_profile_form (Form): The form containing user profile data.

        Returns:
            User: The created user object.

        Raises:
            User.DoesNotExist: If the user with the given username is not found.

        """
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

        return user_form
    
    @staticmethod
    def save_user_info(user_form, user_info_form, user_profile_form, auth_user_instance, user_info_instance):
        """
        Saves the user information and profile data for an existing user.

        Args:
            user_form (Form): The form containing user data.
            user_info_form (Form): The form containing user information data.
            user_profile_form (Form): The form containing user profile data.
            auth_user_instance (User): The existing user instance from the authentication system.
            user_info_instance (UserInfo): The existing user information instance.

        Raises:
            User.DoesNotExist: If the user with the given username is not found.

        """
        # Save user information
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
    