from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        return HttpResponse(form.errors)
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # obține utilizatorul autentificat
            login(request, user)    # loghează utilizatorul
            return redirect('/home')  # redirecționează către o pagină
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})