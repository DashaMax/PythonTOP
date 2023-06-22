from django.urls import path
from .views import get_projects, get_project, create_project, update_project, delete_project


urlpatterns = [
    path('', get_projects, name='projects'),
    path('project/<str:pk>/', get_project, name='project'),
    path('create-project/', create_project, name='create-project'),
    path('update-project/<str:pk>/', update_project, name='update-project'),
    path('delete-project/<str:pk>/', delete_project, name='delete-project')
]
