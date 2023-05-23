from django.http import Http404
from item.models import Item
from category.models import Category


class ItemService:

    @staticmethod
    def get_items_by_category_name(category_name):
        category = Category.objects.filter(name=category_name)
        if len(category) == 0:
            raise Http404("No category with that name")
        category_id = category.get().pk
        try:
            item_list = Item.objects.filter(category_id=category_id)
        except Item.DoesNotExist:
            raise Http404("No items in category.")
        return item_list
