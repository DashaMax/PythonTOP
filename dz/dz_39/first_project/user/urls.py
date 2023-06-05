from django.urls import path

from user.views import get_login, registration, get_logout


urlpatterns = [
    path('login/', get_login, name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', get_logout, name='logout'),
]