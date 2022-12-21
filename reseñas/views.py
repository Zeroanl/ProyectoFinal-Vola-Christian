
from django.views.generic import ListView
from django.views.generic import DetailView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ReseñaClientes
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class ReseñaList(ListView):
    model= ReseñaClientes
    template_name = "reseñas/reseña_list.html"

class ReseñaDetalle(DetailView):
    model = ReseñaClientes
    
@method_decorator(login_required(login_url='/autenticacion/logear'), name='dispatch')
class ReseñaCreate(CreateView):
    model = ReseñaClientes
    fields = "__all__"
    success_url = reverse_lazy("ListaReseñas")
    
@method_decorator(login_required(login_url='/autenticacion/logear'), name='dispatch')
class ReseñaUpdate(UpdateView):
    model = ReseñaClientes
    success_url = reverse_lazy("ListaReseñas")
    fields = "__all__"

@method_decorator(login_required(login_url='/autenticacion/logear'), name='dispatch')    
class ReseñaDelete(DeleteView):
    model = ReseñaClientes
    success_url = reverse_lazy("ListaReseñas")





