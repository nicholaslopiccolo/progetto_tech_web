from django.forms import ModelForm
from .models import Peso

class PesoForm(ModelForm):
    class Meta():
        model = Peso
        fields = ['peso','date']

    def save(self,user):
        peso = self.cleaned_data.get("peso")
        date = self.cleaned_data.get("date")
        Peso(
            peso=peso,
            date=date,
            owner=user
        ).save()