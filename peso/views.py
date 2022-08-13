from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Peso
from .forms import PesoForm


# Create your views here.
@login_required(login_url="/signin")
def home(request):
    form_peso = PesoForm(request.POST or None)

    if request.method == "POST"and form_peso.is_valid():
        peso = form_peso.save(commit=False)
        peso.owner = request.user
        peso.save()

        messages.success(request,"Peso inserito correttamente")
        form_peso = PesoForm()
            
    return render(request, 'peso/form.html',{"form" : form_peso})

@login_required(login_url="/signin")
def delete(request, id=None):
    try:
        Peso.objects.get(pk=id,owner=request.user).delete()
        messages.info(request,"L'elemento è stato eliminato correttamente")
    except Peso.DoesNotExist:
        messages.warning(request,"L'elemento non è stato trovato")

    return redirect('peso-home')

@login_required(login_url="/signin")
def edit(request,id=None):
    try:
        obj=Peso.objects.get(pk=id,owner=request.user)
        form_peso = PesoForm(request.POST or None, request.FILES or None, instance=obj)
        form_peso.date = obj.date
    except Peso.DoesNotExist:
        messages.warning(request,"Oggetto inesistente")
        return redirect("peso-home")

    if request.method == "POST" and form_peso.is_valid():
        peso = form_peso.save(commit=False)
        peso.owner = request.user
        peso.save()

        messages.success(request,"Peso aggiornato correttamente")
        form_peso = PesoForm()
            
    return render(request, 'peso/form.html',{"form" : form_peso,"peso":obj})