from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/watchlist
    path('', views.index, name="watchlist-index"),
    path('add_to_watchlist/<int:itemid>', views.add_to_watchlist, name="add_to_watchlist"),
]

