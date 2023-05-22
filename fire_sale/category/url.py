from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/categories
    path('', views.index, name="category-index"),
]

