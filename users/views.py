from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = forms.CustomUserLogin()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        post = request.POST
        email = post['email']
        password = post['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'home.html')