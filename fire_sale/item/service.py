from django.http import Http404
from item.models import Item
from category.models import CategoryViews, Category
from user.models import User, UserInfo, UserProfile


class ItemService:

    @staticmethod
    def get_items_by_category_name(category_name):
        category = Category.objects.get(name=category_name)
        try:
            item_list = Item.objects.filter(category_id=category.id)
        except Item.DoesNotExist:
            raise Http404("No items in category.")
        return item_list
        
    @staticmethod
    def get_seller_details_from_item_id(item_id):
        item = Item.objects.get(id=item_id)
        user_info = UserInfo.objects.get(user_id=item.seller_id)
        user_profile = UserProfile.objects.get(user_info_id=item.seller_id)
        
        seller_details = {
            "full_name": user_info.user.full_name,
            "avg_rating": user_info.avg_rating,
            "location": f"{user_profile.zip_code}, {user_profile.city}"
        }

        return seller_details

    @staticmethod
    def get_categories_and_items_by_userid(user_id):
        category_views = CategoryViews.objects

        if user_id is None:  # If guest user
            user_category_views = category_views.distinct("category_id")
        else:  # If registered user
            user_category_views = category_views.filter(user_id=user_id)
        
        categories_and_items = []

        for category in user_category_views.all():
            category_id = category.category
            items = Item.objects.filter(category_id=category_id)
            categories_and_items.append({"name": category_id, "items": items})
        
        return categories_and_items


    

    @staticmethod
    def get_category_and_items_by_itemid(item_id):
        category = Item.objects.get(id=item_id).category_id
        items = Item.objects.filter(category_id = category).exclude(id=item_id)
        category_and_items = {"name": category, "items": items}
        return category_and_items
