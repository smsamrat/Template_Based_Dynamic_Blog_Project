from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('write-blog', views.CreateBlogs.as_view(), name='write_blog'),
]
