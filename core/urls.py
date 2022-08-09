from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pasto/", include("peso.urls")),
    path("peso/", include("pasto.urls")),
    path("signin/", views.login_view, name="signin"),
    path("signup/", views.register_user, name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", views.home, name="home")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
