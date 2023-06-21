from django.urls import path

from .views import profiles, user_profile, login_user, logout_user, register, account, edit_account


urlpatterns = [
    path('', profiles, name='profiles'),
    path('profile/<str:pk>', user_profile, name='user_profile'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('account/', account, name='account'),
    path('edit-account/', edit_account, name='edit-account'),
]
