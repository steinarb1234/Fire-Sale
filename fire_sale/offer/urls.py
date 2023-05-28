from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/offers
    path('', views.index, name="offer-index"),
    # path('<int:id>', views.get_item_by_id, name="offer-details")
    path('checkout', views.checkout, name="checkout"),
    path('create_offer/<int:item_id>', views.create_offer, name="create_offer"),
]



