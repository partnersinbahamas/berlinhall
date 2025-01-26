from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from .forms import UserLogin, UserRegister
from django.contrib import messages

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have been successfuly registered!')
            redirect('home')
        else: 
            messages.error(request, 'Opps.. Registation failed')
    else: 
      form = UserRegister()

    data = {
        'form': form
    }

    return render(request, 'user/register.html', data)

def user_login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Welcome! Login success')
            redirect('home')
        else:
            messages.error(request, 'Opps.. Login failed')
    else:
        form = UserLogin()
        
    data = {
        'form': form
    }

    return render(request, 'user/login.html', data)



def user_logout(requset):
    logout(requset)
    return redirect('login')