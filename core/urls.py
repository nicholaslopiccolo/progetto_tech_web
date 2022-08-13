from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pasto.urls")),
    path("peso/", include("peso.urls")),
    path("signin/", views.login_view, name="signin"),
    path("session/",views.get_config,name="session"),
    path("signup/", views.register_user, name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", views.home, name="home")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
