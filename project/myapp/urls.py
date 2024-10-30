from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('requests/', views.request_list, name='request_list'),
    path('requests/<int:request_id>/', views.request_detail, name='request_detail'),
    path('requests/new/', views.request_form, name='request_form'),
    path('users/', views.user_list, name='user_list'),  # List of users
    path('users/new/', views.user_form, name='user_form'),  # Create new user
    path('users/<int:user_id>/', views.user_profile, name='user_profile'),  # User profile
    path('users/edit/<int:user_id>/', views.user_form, name='user_edit'),  
    path('users/<int:user_id>/', views.user_profile, name='user_profile'),
    path('users/<int:user_id>/', views.user_profile, name='user_profile'),
  # User profile
# Edit existing user
]
