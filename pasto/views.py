from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Pasto
from .forms import PastoForm


# Create your views here.
@login_required(login_url="/signin")
def home(request,id=None):
    form_pasto = PastoForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form_pasto.is_valid():
        pasto = form_pasto.save(commit=False)
        pasto.owner = request.user
        pasto.foto = request.FILES.get('foto')
        pasto.save()

        messages.success(request,"Pasto inserito correttamente")
        form_pasto = PastoForm()
            
    return render(request, 'pasto/form.html',{"form" : form_pasto})

@login_required(login_url="/signin")
def delete(request,id=None):
    try:
        Pasto.objects.get(pk=id).delete()
        messages.info(request,"L'elemento è stato eliminato correttamente")
    except Pasto.DoesNotExist:
        messages.warning(request,"L'elemento non è stato trovato")

    return redirect('pasto-home')

@login_required(login_url="/signin")
def details(request,id=None):
    form_pasto = PastoForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form_pasto.is_valid():
        pasto = form_pasto.save(commit=False)
        pasto.owner = request.user
        pasto.foto = request.FILES.get('foto')
        pasto.save()

        messages.success(request,"Pasto inserito correttamente")
        form_pasto = PastoForm()
            
    return render(request, 'pasto/form.html',{"form" : form_pasto})