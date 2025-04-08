from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import (RegisterView,
                         email_verification,
                         UserListView,
                         BlockUserView,
                         UserUpdateView,
                         UserDetailView)

app_name = "users"


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),   # noqa
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),  # noqa
    path("logout/", LogoutView.as_view(next_page="mailing:home"), name="logout"),  # noqa
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),    # noqa
    path("user_list/", UserListView.as_view(), name="user_list"),     # noqa
    path("user_block/<int:user_id>", BlockUserView.as_view(), name="user_block"),   # noqa
    path("user_update/<int:pk>", UserUpdateView.as_view(), name="user_update"),     # noqa
    path("user_profile/<int:pk>", UserDetailView.as_view(), name="user_profile"),    # noqa
]
