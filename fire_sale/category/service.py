from item.service import ItemService

class CategoryService:

    @staticmethod
    def format_items_for_category_page(category_id):
        items = ItemService.get_items_by_category(category_id)
        item_list = []
        for item in items:
            item_list.append({'name': item.name,
                              'price': item.price,
                              'image': item.itemimage_set.first.image})
        return item_list
