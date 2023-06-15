"""
URL configuration for accounts.
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import AllUsersView, RegisterUserView, UserView

urlpatterns = [
    path("api/users/", AllUsersView.as_view()),
    path("api/user/", UserView.as_view()),
    path("api/register/", RegisterUserView.as_view()),
    # JWT authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # session authentication
    # path("api/session/auth/", include("rest_framework.urls", namespace="rest_framework")),
]
