from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        print('hi')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('chest-play')
        else:
            messages.error(request, f'Error!')
        
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Uwierzytelnienie zkaończyło się sukcesem.')
                else:
                    return HttpResponse('Konto jest zablokowane')
        else:
            return HttpResponse('NIeprawidłowe dane uwierzytelniające')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})    

