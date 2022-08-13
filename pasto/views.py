from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Pasto, Commento
from .forms import PastoForm


# Create your views here.
@login_required(login_url="/signin")
def home(request):
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
def edit(request,id=None):
    try:
        obj=Pasto.objects.get(pk=id,owner=request.user)
        form_pasto = PastoForm(request.POST or None, request.FILES or None, instance=obj)
        form_pasto.date = obj.date

    except Pasto.DoesNotExist:
        messages.warning(request,"Oggetto inesistente")
        return redirect("pasto-home")

    if request.method == "POST" and form_pasto.is_valid():
        pasto = form_pasto.save(commit=False)
        pasto.owner = request.user
        pasto.foto = request.FILES.get('foto') or pasto.foto
        pasto.save()

        messages.success(request,"Pasto aggiornato correttamente")
        return redirect("pasto-details",id)
            
    return render(request, 'pasto/form.html',{"form" : form_pasto,"pasto":obj})

@login_required(login_url="/signin")
def delete(request,id=None):
    try:
        Pasto.objects.get(pk=id,owner=request.user).delete()
        messages.info(request,"L'elemento è stato eliminato correttamente")
    except Pasto.DoesNotExist:
        messages.warning(request,"L'elemento non è stato trovato")

    return redirect('pasto-home')

def details(request,id=None):
    try:
        obj=Pasto.objects.get(pk=id,owner=request.user)
    except Pasto.DoesNotExist:
        messages.warning(request,"Oggetto inesistente")
        return redirect("pasto-home")

    commenti=Commento.objects.filter(pasto=obj)

    if request.method == "POST":
        if id:
            messages.success(request,"Pasto aggiornato correttamente")
        else:
            messages.success(request,"Pasto inserito correttamente")
            
    return render(request, 'pasto/details.html',{"pasto" : obj, "commenti":commenti})