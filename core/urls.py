from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from core.views import home, toggle_attivazione_utente, toggle_privilegi_staff, login_view, get_config, register_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("staff/activate/<int:id>",toggle_attivazione_utente,name="staff-toggle-active"),
    path("staff/promote/<int:id>",toggle_privilegi_staff,name="staff-toggle-promote"),
    path("", include("pasto.urls")),
    path("peso/", include("peso.urls")),
    path("signin/", login_view, name="signin"),
    path("session/",get_config,name="session"),
    path("signup/", register_user, name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", home, name="home")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
