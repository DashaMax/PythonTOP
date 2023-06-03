from django.urls import path
from blog.views import blogs, blog


urlpatterns = [
    path('', blogs, name='blogs'),
    path('<int:blog_id>/', blog, name='blog'),
]