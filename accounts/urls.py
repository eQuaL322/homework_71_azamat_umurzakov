from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, SearchAccountListView, \
    AccountDetailView, subscribe_view, unsubscribe_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/search', SearchAccountListView.as_view(), name='account_search'),
    path('<str:username>/', AccountDetailView.as_view(), name='account_detail'),
    path('<str:username>/subscribe', subscribe_view, name='subscribe'),
    path('<str:username>/unsubscribe', unsubscribe_view, name='unsubscribe'),
]
