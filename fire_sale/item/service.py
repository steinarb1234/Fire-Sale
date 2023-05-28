from django.http import Http404
from item.models import Item, ItemImage
from category.models import CategoryViews, Category
from user.models import User, UserInfo, UserProfile


class ItemService:

    @staticmethod
    def get_items_by_category_name(category_name):
        item_list = []
        if category_name == "All":
            item_list = Item.objects.all().values()
            images = ItemImage.objects.all().distinct('item_id').values()
        else:
            try:
                item_list = Item.objects.filter(category_id=category_name).values()
                images = ItemImage.objects.all().filter(item__category_id=category_name).distinct('item_id').values()
            except Item.DoesNotExist:
                raise Http404("No items in category.")

        item_zip = tuple(zip(item_list, images))
        return item_zip
        
    @staticmethod
    def get_seller_details_from_item_id(item_id):
        item = Item.objects.get(id=item_id)
        user_info = UserInfo.objects.get(user_id=item.seller_id)
        user_profile = UserProfile.objects.get(user_info_id=item.seller_id)
        
        seller_details = {
            "username": user_info.user.user_name,
            "full_name": user_info.user.full_name,
            "avg_rating": user_info.avg_rating,
            "location": f"{user_profile.zip_code}, {user_profile.city}"
        }

        return seller_details

    @staticmethod
    def get_categories_and_items_by_userid(user_id):
        category_views = CategoryViews.objects.prefetch_related('category')

        # if user_id is None:  # If guest user
        user_category_views = category_views.distinct("category_id")
        # else:  # If registered user
        #     user_category_views = category_views.filter(user_id=user_id)
        
        categories_and_items = []

        all_items = Item.objects.all()
        for category in user_category_views.all():
            category_id = category.category
            items = all_items.filter(category_id=category_id).values()
            images = ItemImage.objects.all().filter(item__category_id=category_id).distinct('item_id').values()

            items_zip = tuple(zip(items, images))
            # for item, image in items_zip:
            #     print(item, image)
            categories_and_items.append({"name": category_id, "items": items_zip})
        
        return categories_and_items


    

    @staticmethod
    def get_category_and_items_by_itemid(item_id):
        category = Item.objects.get(id=item_id).category_id

        items = Item.objects.filter(category_id=category).exclude(id=item_id)

        images = ItemImage.objects.all().filter(item__category_id=category).distinct('item_id').values()

        items_zip = tuple(zip(items, images))

        category_and_items = {"name": category, "items": items_zip}
        return category_and_items
