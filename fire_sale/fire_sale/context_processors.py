import django.utils.timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg
from django.shortcuts import resolve_url

from category.models import Category
from rating.models import Rating
from user.models import User, Notification


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
            user_instance = User.objects.get(id=user.id)# Laga með id
        except:
            print(f"""\n\n
                    Could not find a user in User.objects.
                    user.username: {user.username} \n\n
            """)

    return {'user_instance': user_instance}


def notifications_processor(request):
    notifications = Notification.objects.filter(receiver=request.user.id, seen=False)

    for notification in notifications:
        if notification.href_parameter:
            notification.href = resolve_url(notification.href, notification.href_parameter)
        else:
            notification.href = resolve_url(notification.href)

    return {'notifications': notifications}



def user_rating_processor(request):
    user_ratings = Rating.objects.filter(offer__seller_id=request.user.id)
    if user_ratings:
        average_rating = round(list(user_ratings.aggregate(Avg('rating')).values())[0], 1)
        return {
            "user_ratings": user_ratings,
            'average_rating': average_rating
        }
    else:
        return {
            "user_ratings": user_ratings,
        }

