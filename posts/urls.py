from django.urls import path

from posts.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/create', PostCreateView.as_view(), name='post_create')
]
