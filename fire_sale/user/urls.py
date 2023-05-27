from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/user
    path('my_offers/', views.my_offers, name='my_offers'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='user-profile'),
    path('', views.profile, name='user-profile'),
    # path('my_offers', views.my_offers, name='my_offers'),

]