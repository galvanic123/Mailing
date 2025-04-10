from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.services import block_user
from users.views import (
    PasswordRecoveryView, UserCreateView,
    UserDeleteView, UserDetailView, UserListView,
    UserUpdateView, email_verification, user_logout
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "login/", LoginView.as_view(template_name="users/login.html"), name="login" # noqa
    ),
    path("logout/", user_logout, name="logout"),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="reset_password"  # noqa
    ),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),     # noqa
    path("register/", UserCreateView.as_view(), name="register"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("detail/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
    path(
        "password-recovery/", PasswordRecoveryView.as_view(), name="password_recovery"    # noqa
    ),
    path("block_user/<int:pk>", block_user, name="block_user"),
]
