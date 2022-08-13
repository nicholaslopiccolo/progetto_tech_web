from django.urls import path
from .views import home, edit, delete
from .ajax_datatable_views import PesoAjaxDatatableView

urlpatterns = [
    path("ajax_datatable/", PesoAjaxDatatableView.as_view(), name="ajax_datatable_peso"),
    path("",home,name="peso-home"),
    path("<id>", edit, name="peso-home"),
    path("delete/<id>", delete, name="peso-delete"),
]