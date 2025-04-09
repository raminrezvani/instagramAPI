from django.urls import path
from .views import SignUpView, SignInView, UserListView, PublicUserListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('users/', UserListView.as_view(), name='users'),
    path('public-users/', PublicUserListView.as_view(), name='public-users'),
]