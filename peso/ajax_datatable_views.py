from django.core.exceptions import PermissionDenied
from ajax_datatable import AjaxDatatableView
from .models import Peso

from django.urls import reverse



class PesoAjaxDatatableView(AjaxDatatableView):

    model = Peso
    title = 'Pesate'
    initial_order = [["date", "dsc"], ]
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'searchable':False, 'visible': False, },
        {'name': 'date', 'visible': True, },
        {'name': 'peso', 'visible': True, },
        {'name': 'edit', 'title': 'Edit', 'placeholder': True, 'searchable': False, 'orderable': False, },
    ]

    
    def get_initial_queryset(self, request=None):

        if not request.user.is_authenticated:
            raise PermissionDenied

        # We accept either GET or POST
        if not getattr(request, 'REQUEST', None):
            request.REQUEST = request.GET if request.method=='GET' else request.POST

        queryset = self.model.objects.all()

        
        user = request.user
        queryset = queryset.filter(owner=user)

        return queryset

    def customize_row(self, row, obj):
        row['edit'] = """
            <div class="field has-addons">
                <p class="control">
                    <a class="button is-info" href="{0}">
                        <span class="icon">
                            <i class="fa-solid fa-pen"></i>
                        </span>
                    </a>
                </p>
                <p class="control">
                    <a class="button is-danger" href="{1}">
                        <span class="icon">
                            <i class="fa-solid fa-trash-can"></i>
                        </span>
                    </a>
                </p>
            </div>
        """.format(reverse('peso-home',kwargs={'id': obj.id}),reverse('peso-delete',kwargs={'id': obj.id}))