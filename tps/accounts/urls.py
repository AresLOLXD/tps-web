from django.urls import re_path
from accounts import views


urlpatterns = [
    re_path(r"^profile", views.view_profile, name="profile"),
    re_path(r"^password", views.change_password, name="change_password"),
    re_path(r"^login/$", views.login, name="login"),
    re_path(r"^logout/$", views.logout, name="logout"),
]
