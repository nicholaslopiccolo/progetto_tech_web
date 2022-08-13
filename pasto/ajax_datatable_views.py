from django.core.exceptions import PermissionDenied
from ajax_datatable import AjaxDatatableView
from .models import Pasto

from django.urls import reverse



class PastoAjaxDatatableView(AjaxDatatableView):

    model = Pasto
    title = 'Pasti'
    initial_order = [["date", "dsc"], ]
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'searchable':False, 'visible': False, },
        {'name': 'date', 'visible': True, },
        {'name': 'descrizione', 'visible': True, },
        {'name': 'kcal', 'searchable':False, 'visible': True, },
        {'name': 'tipo',  'visible': True, },
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
                    <a class="button" href="{0}">
                        <span class="icon">
                            <i class="fa-solid fa-info" style="font-size:1.5rem"></i>
                        </span>
                    </a>
                </p>
                <p class="control">
                    <a class="button is-info" href="{1}">
                        <span class="icon">
                            <i class="fa-solid fa-pen"></i>
                        </span>
                    </a>
                </p>
                <p class="control">
                    <a class="button is-danger" href="{2}">
                        <span class="icon">
                            <i class="fa-solid fa-trash-can"></i>
                        </span>
                    </a>
                </p>
            </div>
        """.format(reverse('pasto-details',kwargs={'id': obj.id}),reverse('pasto-home',kwargs={'id': obj.id}),reverse('pasto-delete',kwargs={'id': obj.id}))