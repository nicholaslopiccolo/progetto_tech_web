from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import PesoForm


# Create your views here.
@login_required(login_url="/signin")
def home(request):
    form_peso = PesoForm(request.POST or None)

    if request.method == "POST"and form_peso.is_valid():
        form_peso.save(request.user)

        messages.success(request,"Pasto inserito correttamente")
        form_peso = PesoForm()
            
    return render(request, 'peso/form.html',{"form" : form_peso})