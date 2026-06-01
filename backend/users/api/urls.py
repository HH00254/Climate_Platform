from django.urls import path

from users.api.views import (
    UserRegistrationView,
    UserLoginView,
    CurrentUserView
)

urlpatterns = [
    path(
        "register/",
        UserRegistrationView.as_view(),
        name="register"
    ),

    path(
        "login/",
        UserLoginView.as_view(),
        name="login"
    ),

    path(
        "me/",
        CurrentUserView.as_view(),
        name="current-user"
    ),
]