from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('write-blog', views.CreateBlogs.as_view(), name='write_blog'),
]
