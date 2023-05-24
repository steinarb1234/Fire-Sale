from django.http import Http404
from item.models import Item
from category.models import Category
from user.models import User, UserInfo, UserProfile


class ItemService:

    @staticmethod
    def get_items_by_category_name(category_name):
        category = Category.objects.get(name=category_name)
        try:
            item_list = Item.objects.filter(category_id = category.id)
        except Item.DoesNotExist:
            raise Http404("No items in category.")
        return item_list
        
    @staticmethod
    def get_seller_details_from_item_id(item_id):
        item = Item.objects.get(id = item_id)
        user_info = UserInfo.objects.get(user_id = item.seller_id)
        user_profile = UserProfile.objects.get(user_info_id = item.seller_id)
        
        seller_details = {
            "full_name": user_info.full_name,
            "avg_rating": user_info.avg_rating,
            "location": f"{user_profile.zip_code}, {user_profile.city}"
        }

        return seller_details
