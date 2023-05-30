from category.models import Category
from user.models import User, Notifications


# from django.views.decorators.cache import cache_page

# @cache_page(600)
def categories_processor(request):
    categories = Category.objects.all().prefetch_related('parent')
    return {'categories': categories}

def navigation_bar_processor(request):
    user = request.user
    user_instance = None

    if user.is_authenticated and hasattr(user, 'username'):
        try:
            user_instance = User.objects.get(id = user.id)# LAga með id
        except:
            print(f"""\n\n
                    Could not find a user in User.objects.
                    user.username: {user.username} \n\n
            """)

    return {'user_instance': user_instance}


def notifications_processor(request):
    notifications = Notifications.objects.filter(receiver=request.user.id)
    return {'notifications': notifications}



