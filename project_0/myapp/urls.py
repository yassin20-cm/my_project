from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('requests/', views.request_list, name='request_list'),
    path('requests/new/', views.request_form, name='request_form'),
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_form, name='user_form'),
    path('users/<int:user_id>/', views.user_form, name='user_edit'),
    path('profile/', views.user_profile, name='profile'),
    path('requests/', views.request_list, name='request_list'),
    path('requests/<int:request_id>/', views.request_detail, name='request_detail'),
    path('users/<int:user_id>/', views.user_profile, name='user_profile'),
    path('users/new/', views.user_form, name='user_form'),  # For creating a new user
    path('users/<int:user_id>/', views.user_form, name='user_detail'),  # For viewing/editing an existing user
    path('users/', views.user_list, name='user_list'), 
    path('requests/new/', views.request_form, name='request_form'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),  
]
