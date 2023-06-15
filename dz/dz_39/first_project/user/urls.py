from django.urls import path

from user.views import get_login, registration, get_logout, get_lk, get_mypassword, add_password, delete


urlpatterns = [
    path('login/', get_login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', get_logout, name='logout'),
    path('lk/', get_lk, name='lk'),
    path('add_password/', add_password, name='add_password'),
    path('mypassword/', get_mypassword, name='mypassword'),
    path('delete/<int:pk>/', delete, name='delete'),
]