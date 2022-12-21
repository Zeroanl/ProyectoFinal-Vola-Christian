from django.shortcuts import render
from avatar.models import Avatar
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user = request.user.id)
    return render(request,"ProyectoFinalApp/base.html", {"url":avatares[0].imagen.url})


