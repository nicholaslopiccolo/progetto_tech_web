import json

from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Pasto, Commento, LikeCommento, LikePasto
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
        obj=Pasto.objects.get(pk=id)
    except Pasto.DoesNotExist:
        messages.warning(request,"Oggetto inesistente")
        return redirect("pasto-home")

    commenti = obj.gen_tree_commenti()
            
    return render(request, 'pasto/details.html',{"pasto" : obj, "commenti":commenti})

@login_required(login_url="/signin")
def create_commento(request,pasto=None,commento=None):
    try:
        pasto = Pasto.objects.get(pk=pasto)
    except Pasto.DoesNotExist:
        messages.error(request,"Dati mancanti")
        return redirect("pasto-home")

    try:
        commento = Commento.objects.get(pk=commento)
    except Commento.DoesNotExist:
        # Commento non reply
        commento = None

    if request.method == "POST":
        Commento(
            commento=request.POST.get("commento"),
            pasto=pasto,
            owner=request.user,
            reply=commento
        ).save()
        messages.success(request,"Commento inserito correttamente.")
        return redirect("pasto-details",pasto.pk)
    else:
        return render(request, 'pasto/reply.html',{"pasto" : pasto, "commento":commento}) 

@login_required(login_url="/signin")
def toggle_like_commento(request, commento=None):
    if commento:
        commento=Commento.objects.get(pk=commento)
        try:
            LikeCommento.objects.get(commento=commento,owner=request.user).delete()
            messages.success(request,"LIKE AL COMMENTO ELIMINATO")
        except LikeCommento.DoesNotExist:
            LikeCommento(commento=commento,owner=request.user).save()
            messages.success(request,"LIKE AL COMMENTO AGGIUNTO")
        return redirect("pasto-details", commento.pasto.pk)
    return redirect("pasto-home")

@login_required(login_url="/signin")
def toggle_like_pasto(request, pasto=None):
    if pasto:
        pasto=Pasto.objects.get(pk=pasto)
        try:
            LikePasto.objects.get(pasto=pasto,owner=request.user).delete()
            messages.success(request,"LIKE AL PASTO ELIMINATO")
        except LikePasto.DoesNotExist:
            LikePasto(pasto=pasto,owner=request.user).save()
            messages.success(request,"LIKE AL PASTO AGGIUNTO")
        return redirect("pasto-details", pasto.pk)
    return redirect("pasto-home")

def pasto_search(request):
    if request.method == "POST":
        # Input dell'utente
        pasto_text =  json.loads(request.body.decode('utf-8')).get("text").strip()
        # Ritorna solo le 10 più importanti
        raw_results = Pasto.objects.filter(descrizione__contains=pasto_text)[:10]
        if request.user.is_authenticated:
            results = [{'descrizione':el.descrizione,'url':reverse("pasto-details",args=[el.pk]),'kcal':el.kcal,'owner':el.owner.username} for el in raw_results]
        else:
            results = [{'descrizione':el.descrizione,'url':reverse("pasto-details",args=[el.pk]),'kcal':el.kcal} for el in raw_results]

        return JsonResponse({'res':results})
    return JsonResponse({'error':"404"})