from django.urls import path, include
from . import views

urlpatterns = [
    # http://localhost:8000/items
    path('', views.index, name="item-index"),
    path('<int:id>', views.get_item_details_by_id, name="item-details"),
    path('create_item', views.create_item, name="create-item"),
    path('delete_item/<int:id>', views.delete_item, name="delete-item"),
    path('edit_item/<int:id>', views.edit_item, name="edit-item"),
    path('<int:item_id>/offers', views.item_offers, name="item-offers"),
    path('<int:item_id>/offers_buyer_view', views.item_offers_buyers, name="item-offers-buyers")
]

