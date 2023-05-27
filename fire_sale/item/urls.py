from django.urls import path, include
from . import views

urlpatterns = [
    # http://localhost:8000/items
    path('', views.index, name="item-index"),
    path('<int:id>', views.get_item_details_by_id, name="item-details"),
    path('create_item', views.create_item, name="create_item"),
    path('delete_item/<int:id>', views.delete_item, name="delete_item"),
    path('edit_item/<int:id>', views.edit_item, name="edit_item"),
    path('__debug__/', include('debug_toolbar.urls')),
]

