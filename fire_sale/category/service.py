from category.models import Category
from watchlist.models import WatchListItem
from item.models import Item, ItemImage, ItemStats
from django.db.models import Prefetch, Q, Exists, OuterRef


class CategoryService:
    @staticmethod
    def get_search_results(category_name, query, user=None):
        items = Item.objects.all().prefetch_related(
            Prefetch('itemimage_set', queryset=ItemImage.objects.all().order_by('id')),
        )

        if category_name and category_name != "All":
            category_query = Q(category__name=category_name)
            subcategories = Category.objects.filter(parent=category_name)
            for subcategory in subcategories:
                category_query.add(Q(category__name=subcategory), Q.OR)
            items = items.filter(category_query)

        if query:
            items = items.filter(name__icontains=query)

        items = items.filter(itemstats__status='Not sold')

        if user:
            watchlist_items = WatchListItem.objects.filter(user_id=user.id)
            items = items.annotate(is_in_watchlist=Exists(watchlist_items.filter(item_id=OuterRef('pk'))))

        return items
