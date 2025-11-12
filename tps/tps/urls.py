import debug_toolbar
from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^", include("problems.urls", namespace="problems")),
    re_path(r"^accounts/", include("accounts.urls", namespace="accounts")),
    re_path(r"^__debug__/", include(debug_toolbar.urls)),
]
