from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return render(request, 'home.html')


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            return redirect('/')
        else:
            msg = 'Invalid credentials'   

    return render(request, "user/signin.html", {"form": form, "msg" : msg})

def register_user(request):
    form = UserCreationForm(data=request.POST or None)

    msg = ''
    success = False

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")

        else:
            for m in form.error_messages:
                msg = msg + '\n' +form.error_messages.get(m)
                #messages.error(request, f'{msg}: {form.error_messages[msg]}')
            #return render(request,
                          #template_name='main/register.html',
                          #context={'form': form})
            #msg = 'Form non valido'  

    return render(request, "user/signup.html", {"form": form, "msg" : msg, "success" : success })