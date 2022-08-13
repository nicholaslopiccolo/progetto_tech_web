from django.forms import ModelForm, Textarea
from django import forms
from .models import Pasto, Commento

class PastoForm(ModelForm):
    class Meta():
        model = Pasto
        fields = ['kcal','date','descrizione','tipo','foto','owner']
        widgets = {
            'descrizione':Textarea(attrs={'class':"textarea",'cols':80,'rows':5}),
            'date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'input','type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(PastoForm,self).__init__(*args, **kwargs)
        self.fields['tipo'].widget=forms.Select(choices=Pasto.TIPI_DI_PASTO)
        self.fields['foto'].required = False
        self.fields['owner'].required = False
