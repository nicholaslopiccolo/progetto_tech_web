from django.urls import path, include
from .views import home,delete,details,edit

from .ajax_datatable_views import PastoAjaxDatatableView

urlpatterns = [
    path("pasto/ajax_datatable/", PastoAjaxDatatableView.as_view(), name="ajax_datatable_pasto"),
    path("pasto/", home, name="pasto-home"),
    path("pasto/<id>", edit, name="pasto-home"),
    path("pasto/details/<id>", details, name="pasto-details"),
    path("pasto/delete/<id>", delete, name="pasto-delete"),
]




