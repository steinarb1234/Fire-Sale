from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/listings
    path('', views.index, name="item-index"),
    path('<int:id>', views.get_item_by_id, name="item-details")
]

