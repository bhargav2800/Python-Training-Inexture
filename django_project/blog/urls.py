from os import abort
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # <app>/<model>_<view_type>.html  --  PostListView will search for blog/post_list.html   so, we have to replace it by providing template_name in Views.py
    path('', PostListView.as_view(), name='blog-home'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    # <app>/<model>_<view_type>.html  --  PostListView will search for blog/post_detail.html   So, just create post_detail.html file in templeates/blog .
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Will Search for post_form.html in templates/blog   so, let's create it
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    
    # Expact the form  --->>   post_confirm_delete.html   ... Let's Create
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about')
]
