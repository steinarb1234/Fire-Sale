from item.models import Item, ItemImage
from django.db.models import Prefetch

class CategoryService:
 
    @staticmethod
    def get_search_results(category_name, query):
        items = Item.objects.all().prefetch_related(
            Prefetch('itemimage_set', queryset=ItemImage.objects.all().order_by('id'))
        )

        if category_name and category_name != "All":
            items = items.filter(category__name=category_name)

        if query:
            items = items.filter(name__icontains=query)

        return items