from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/watchlist
    path('', views.index, name="watchlist-index"),
    path('add_to_watchlist/<int:item_id>', views.add_to_watchlist, name="add_to_watchlist"),
    path('delete_from_watchlist/<int:item_id>', views.delete_from_watchlist, name="delete_from_watchlist"),
]

