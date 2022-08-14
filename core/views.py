from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
                
        return render(request, 'home.html',{"forms":{"form_pasto":form_pasto,"form_peso":form_peso}})
    return render(request, 'home.html')

def get_config(request):
    if request.user.is_authenticated:
        user = request.user
        return JsonResponse({"username":user.username,"id":user.pk})
    else:
        return HttpResponseForbidden()

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)

    msg = None

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

    msg = ''
    success = False

    if request.method == "POST":
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect("/")

        else:
            messages.error(request,'Form non valido')

    return render(request, "user/signup.html", {"form": form, "msg" : msg, "success" : success })