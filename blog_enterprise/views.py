
from django.shortcuts import redirect, render
from .forms import RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group


def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #asignando grupo de permiso al usuario proveniente del form
            user = form.save()
            group = Group.objects.get(name='blog_group') #el blog_group viene de los permisos asignados.
            group.user_set.add(user)            
                        
            return redirect('register')
    else:
        form = RegistrationForm()
        
    context = {
        'form': form
    }

    return render(request, 'auth/register.html', context)

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
               auth.login(request, user) 
            return redirect('home')      
            
    form = AuthenticationForm()
    
    context = {
        'form': form
    }
    
    return render(request, 'auth/login.html', context)


def logout(request):
    
    auth.logout(request)
    
    return redirect('home')