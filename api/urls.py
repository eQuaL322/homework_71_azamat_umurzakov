from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PostListCreateView, PostGetUpdateDeleteView, PostLikeView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostGetUpdateDeleteView.as_view()),
    path('posts/<int:pk>/like/', PostLikeView.as_view()),
    path('login/', obtain_auth_token, name='obtain_auth_token')

]
