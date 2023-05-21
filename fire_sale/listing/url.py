
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/listings
    path('', views.index, name="index"),
]

