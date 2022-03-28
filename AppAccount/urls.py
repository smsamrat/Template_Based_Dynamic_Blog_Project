from django.urls import path
from AppAccount import views

urlpatterns = [
    path('signup/', views.auth_signup, name='signup'),
    path('login/', views.auth_login, name='login'),
    path('logout/', views.auth_logout, name='logout'),
    path('user-Profile/', views.user_Profile, name='user_Profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('edit-password/', views.edit_password, name='edit_password'),
    path('add-profile-picture/', views.add_profile_picture, name='add_profile_picture'),
    path('edit-profile-picture/', views.edit_profile_picture, name='edit_profile_picture'),
]
