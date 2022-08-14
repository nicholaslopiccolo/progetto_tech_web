from django.urls import path, include
from .views import home,delete,details,edit,create_commento,toggle_like_pasto,toggle_like_commento,pasto_search

from .ajax_datatable_views import PastoAjaxDatatableView

urlpatterns = [
    path("pasto/ajax_datatable/", PastoAjaxDatatableView.as_view(), name="ajax_datatable_pasto"),
    path("pasto/", home, name="pasto-home"),
    path("pasto/<int:id>", edit, name="pasto-home"),
    path("pasto/details/<int:id>", details, name="pasto-details"),
    path("pasto/delete/<int:id>", delete, name="pasto-delete"),
    path("pasto/reply/<int:pasto>", create_commento, name="pasto-reply"),
    path("pasto/reply/<int:pasto>/<int:commento>", create_commento, name="pasto-reply"),
    path("pasto/like/<int:pasto>", toggle_like_pasto, name="pasto-like"),
    path("pasto/reply/like/<int:commento>", toggle_like_commento, name="pasto-reply-like"),
    path("pasto/search/", pasto_search, name="pasto-search"),
]