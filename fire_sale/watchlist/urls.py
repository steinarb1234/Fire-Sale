from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/watchlist
    path('', views.index, name="watchlist-index"),
]
