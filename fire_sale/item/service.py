from django.http import Http404
from item.models import Item, ItemImage, ItemStats
from category.models import CategoryViews, Category
from user.models import User, UserInfo, UserProfile
from watchlist.models import WatchListItem
from django.db.models import Prefetch, Count, Case, When, IntegerField, Exists, OuterRef


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
        item = Item.objects.select_related('seller__userinfo__user', 'seller__userinfo__userprofile').get(id=item_id)

        seller = item.seller
        user_info = seller.userinfo
        user = user_info.user
        user_profile = user_info.userprofile

        seller_details = {
            "username": user.user_name,
            "full_name": user.full_name,
            "avg_rating": user_info.avg_rating,
            "location": f"{user_profile.zip_code}, {user_profile.city}"
        }
        return seller_details

    @staticmethod
    def get_categories_and_items_by_userid(user_id):
        categories = Category.objects.prefetch_related(
            Prefetch('item_set', queryset=Item.objects.prefetch_related('itemimage_set', 'itemstats'))
        )

        categories_and_items = []
        for category in categories:
            items = category.item_set.all()
            categories_and_items.append({"name": category.name, "items": items})

        return categories_and_items

    @staticmethod
    def get_category_and_items_by_itemid(category, item_id, user=None):
        items = Item.objects.filter(category=category).exclude(id=item_id).prefetch_related('itemimage_set', 'itemstats')

        if user:
            watchlist_items = WatchListItem.objects.filter(user=user)
            items = items.annotate(is_in_watchlist=Exists(watchlist_items.filter(item_id=OuterRef('pk'))))

        category_and_items = {"name": category.name, "items": items}
        return category_and_items