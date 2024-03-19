from django.shortcuts import render
from registro import forms, models

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            login(request, user)

            return render(request, 'login.html', {'mensaje': f'Bienvenido {user.username}'})
            
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form':form})

def register(request):

    if request.method == 'POST':
        form = forms.UserCreationFormCustom(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'register.html', {'mensaje':'Te has registrado correctamente'})
        
    else:
        form = forms.UserCreationFormCustom()
    
    return render(request, 'register.html', {'form':form})

def editProfile(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = forms.UserEditForm(request.POST, request.FILES, instance = request.user)

        if formulario.is_valid():

            if hasattr(usuario, 'avatar'): 
                formulario.cleaned_data.get('imagen')
                usuario.avatar.imagen = formulario.cleaned_data.get('imagen')
                usuario.avatar.save()
            
            else:
                models.Avatar.objects.create(user = usuario, imagen = formulario.cleaned_data.get('imagen'))

            formulario.save()

            return render(request, 'editProfile.html', {'mensaje':'Usuario editado correctamente'})
        
    else:
        formulario = forms.UserEditForm(instance = request.user)

    return render(request, 'editProfile.html', {'formulario':formulario,'usuario':usuario})

class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'changePassword.html'
    success_url = reverse_lazy('editProfile')