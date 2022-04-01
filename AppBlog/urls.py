from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('write-blog', views.CreateBlogs.as_view(), name='write_blog'),
    path('<str:slug>/', views.blog_details, name='blog_details'),
    # path('<slug:post(any name)>/', views.blog_details, name='blog_details'), Another slug url
    path('Update-Comment/<pk>/', views.UpdateComment.as_view(), name='update_comment'),
    path('liked/<pk>/',views.blog_liked, name="blog_like"),
    path('disliked/<pk>/',views.blog_disliked, name="blog_dislike"),
    

]
