"""
URL configuration for accounts.
"""

from django.urls import path

from backend.accounts.views import (
    ChangePasswordView,
    UserAvatarAPIView,
    UserView,
)

urlpatterns = [
    # user
    path("api/user/", UserView.as_view(), name="user"),
    path("api/user/change-password", ChangePasswordView.as_view(), name="change_password"),
    # profile
    path("api/profile/avatar/", UserAvatarAPIView.as_view(), name="user_avatar"),
]
