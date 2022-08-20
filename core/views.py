from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User


from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from pasto.models import Pasto, Commento, LikePasto, LikeCommento
from pasto.forms import PastoForm
from peso.forms import PesoForm

from django.contrib import messages

from django.http import JsonResponse,HttpResponseForbidden

def home(request):
    if request.user.is_authenticated:
        form_pasto = PastoForm(request.POST or None)
        form_peso = PesoForm(request.POST or None)

        if request.method == "POST":
            if form_pasto.is_valid():
                form_pasto.save(request.user)

                messages.success(request,"Pasto inserito correttamente")
                form_pasto = PastoForm()

            if form_peso.is_valid():
                form_peso.save(request.user)

                messages.success(request,"Peso inserito correttamente")
                form_peso = PesoForm()
        # dashboard kcal totali
        d = datetime.today().date() 
        kcal_tot = sum([p.kcal for p in Pasto.objects.filter(owner=request.user,date=d)])

        # dashboard kcal su tipo
        tipo_1 = sum([el.kcal for el in Pasto.objects.filter(owner=request.user,tipo=1)])
        tipo_2 = sum([el.kcal for el in Pasto.objects.filter(owner=request.user,tipo=2)])
        tipo_3 = sum([el.kcal for el in Pasto.objects.filter(owner=request.user,tipo=3)])
        tipo_4 = sum([el.kcal for el in Pasto.objects.filter(owner=request.user,tipo=4)])

        tot_kcal = tipo_1+tipo_2+tipo_3+tipo_4+1


        data = {
            'labels':[el[1] for el in Pasto.TIPI_DI_PASTO],
            'data':[float(el) for el in [
                "{:.1f}".format(tipo_1*100/tot_kcal),
                "{:.1f}".format(tipo_2*100/tot_kcal),
                "{:.1f}".format(tipo_3*100/tot_kcal),
                "{:.1f}".format(tipo_4*100/tot_kcal)
                ]
            ]
        }

        # dashboard like totali pasti e commenti
        like_pasti = LikePasto.objects.filter(pasto__in=Pasto.objects.filter(owner=request.user)).count()
        like_commenti = LikeCommento.objects.filter(commento__in=Commento.objects.filter(owner=request.user)).count()
        if request.user.is_staff:
            return render(request, 'home.html',{"utenti":User.objects.all(),"totale_pasti":Pasto.objects.filter(owner=request.user).count(),"grafo_kcal_tipo":data,"kcal_totali":kcal_tot,"like_pasti":like_pasti,"like_commenti":like_commenti,"forms":{"form_pasto":form_pasto,"form_peso":form_peso}})
        else:
            return render(request, 'home.html',{"totale_pasti":Pasto.objects.filter(owner=request.user).count(),"grafo_kcal_tipo":data,"kcal_totali":kcal_tot,"like_pasti":like_pasti,"like_commenti":like_commenti,"forms":{"form_pasto":form_pasto,"form_peso":form_peso}})
    return render(request, 'home.html')

def get_config(request):
    if request.user.is_authenticated:
        user = request.user
        return JsonResponse({"username":user.username,"id":user.pk})
    else:
        return HttpResponseForbidden()

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request,"Login avvenuto con successo")
            return redirect('/')
        else:
            messages.error(request,'Username o password errati')

    return render(request, "user/signin.html", {"form": form})

def register_user(request):
    form = UserCreationForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("/")

        else:
            messages.error(request,'Form non valido')

    return render(request, "user/signup.html", {"form": form })