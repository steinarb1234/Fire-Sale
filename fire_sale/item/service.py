from django.http import Http404
from item.models import Item, ItemImage
from category.models import CategoryViews, Category
from user.models import User, UserInfo, UserProfile
from django.db.models import Prefetch, Count, Case, When, IntegerField, OuterRef


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
        categories = Category.objects.prefetch_related(
            Prefetch('item_set', queryset=Item.objects.prefetch_related('itemimage_set'))
        )

        categories_and_items = []
        for category in categories:
            items = category.item_set.all()
            categories_and_items.append({"name": category.name, "items": items})

        return categories_and_items

    @staticmethod
    def get_category_and_items_by_itemid(item_id):
        category = Category.objects.get(item__id=item_id)

        items = Item.objects.filter(category=category).exclude(id=item_id)
        item_ids = items.values_list("id", flat=True)

        item_images = ItemImage.objects.filter(item_id__in=item_ids)

        items = items.prefetch_related(Prefetch("itemimage_set", queryset=item_images))

        category_and_items = {"name": category.name, "items": items}

        return category_and_items
