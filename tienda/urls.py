from django.urls import path
from tienda import views


urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('busqueda/', views.busqueda_productos, name="Busqueda"),
    path('buscar/', views.buscar, name="Buscar"),
    path('agradecimiento/', views.agradecimiento, name="agradecimiento"),
    path('detalle/<int:producto_id>/', views.detalles_productos, name="detalle"),
   
]
