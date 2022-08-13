from django.forms import ModelForm, DateInput

from .models import Peso

class PesoForm(ModelForm):
    class Meta():
        model = Peso
        fields = ['peso','date','owner']
        widgets = {
            'date': DateInput(format=('%Y-%m-%d'), attrs={'class':'input','type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(PesoForm,self).__init__(*args, **kwargs)
        self.fields['owner'].required = False