from django.urls import path

from posts.views import PostListView, PostCreateView, PostDetailView, PostLikeView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/like', PostLikeView.as_view(), name='like'),
    path('post/<int:pk>/comment/add', CommentCreateView.as_view(), name='comment_add'),
]
