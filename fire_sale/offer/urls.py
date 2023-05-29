from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/offers
    # path('', views., name="offer-index"),
    path('<int:offer_id>', views.offer_details, name="offer-details"),
    path('<int:offer_id>/checkout', views.checkout, name="checkout"),
    path('create_offer/<int:item_id>', views.create_offer, name="create_offer"),
    path('<int:offer_id>/checkout/payment', views.payment, name="payment"),
    path('<int:offer_id>/checkout/payment/review', views.review, name="review"),
    path('change_offer_stats/<int:id>/<str:button>/', views.change_offer_status, name="change_offer_status"),
]


