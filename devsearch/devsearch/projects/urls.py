from django.urls import path
from .views import get_projects, get_project


urlpatterns = [
    path('', get_projects, name='projects'),
    path('project/<str:pk>/', get_project, name='project')
]