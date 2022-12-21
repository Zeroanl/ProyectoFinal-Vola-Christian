from django.urls import path
from .views import VRegistro, cerrar_sesion,logear,editar_Perfil,editar_password,editar_avatar


urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    path('editar', editar_Perfil, name="editar"),
    path('editarpass', editar_password, name="editarpass"),
    path('editaravatar', editar_avatar, name="editaravatar"),
    
]