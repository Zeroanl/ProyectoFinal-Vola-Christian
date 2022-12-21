from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, UserEditForm, SetPasswordForm,AvatarFormulario
from django.contrib.auth.decorators import login_required
from avatar.models import Avatar
from django.contrib.auth.models import User



# Create your views here.

class VRegistro(View):

    def get(self, request):
        form=CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form":form})

    def post(self, request):
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():
           form.save()
           messages.success(self.request, f'Usuario Registrado con Exito')
           return redirect('Autenticacion')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "registro/registro.html", {"form":form})


def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario no Valido")
        else:
            messages.error(request, "Informacion Incorrecta")

    form=AuthenticationForm()
    return render(request, "login/login.html", {"form":form})

@login_required
def editar_Perfil(request):
    usuario=request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion["email"]
            usuario.last_name = informacion["last_name"]
            usuario.first_name = informacion["first_name"]
            usuario.save()

            messages.success(request, f'Usuario Editado con Exito')

            return render(request,"ProyectoFinalApp/home.html")
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request,"editar/editarperfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def editar_password(request):
    usuario=request.user
    if request.method == 'POST':
        form = SetPasswordForm(usuario, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Password Editada con Exito')
            logout(request)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

    form = SetPasswordForm(usuario)
    
    return render(request,"editar/editarpass.html", {"form":form})


@login_required
def editar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario (request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar (user=u , imagen = form.cleaned_data["imagen"])
            avatar.save()
            messages.success(request, f'Avatar Editado con Exito')
            return redirect('Home') 
    else:
        form = AvatarFormulario ()
    
    return render (request,"editar/editaravatar.html", {"form":form})