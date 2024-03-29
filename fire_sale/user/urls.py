from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/user

    # path('', views.user_profile, name='user-profile'),
    path('my_offers/', views.my_offers, name='my-offers'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.user_profile, name='user-profile'),
    path('update_profile/<int:id>', views.update_profile, name="update_profile"),
    path('my_listings', views.my_listings, name="my-listings"),
    path('notifications/', views.notifications, name="notifications"),
    path('<str:notification_id>', views.mark_notification_as_seen, name='mark_notification_as_seen'),
]