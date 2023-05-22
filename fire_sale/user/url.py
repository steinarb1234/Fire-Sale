from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/users
    path('', views.index, name="item-index"),
]