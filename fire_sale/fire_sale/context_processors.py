from category.models import Category
from user.models import User


def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}

def navigation_bar_processor(request):
    user = request.user
    profile_image_url = ''

    if user.is_authenticated and hasattr(user, 'username'):
        try:
            user_instance = User.objects.get(user_name = user.username)
            profile_image_url = user_instance.userinfo.image
        except:
            print(f"""\n\n
                    Could not find a user in User.objects.
                    user.username: {user.username} \n\n
            """)

    return {'profile_image_url': profile_image_url}