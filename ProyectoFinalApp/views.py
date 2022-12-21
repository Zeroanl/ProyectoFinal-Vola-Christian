from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request,"ProyectoFinalApp/home.html")


def aboutme(request):
    return render(request,"ProyectoFinalApp/aboutme.html")





