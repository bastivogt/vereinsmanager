from django.urls import path

from django.contrib.auth import views as auth_views

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="sevo_auth/login.html"), name="sevo-auth-login"),
    path("logout/", auth_views.LogoutView.as_view(), name="sevo-auth-logout"),
]


