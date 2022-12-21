from django.urls import path
from reseñas.views import ReseñaList, ReseñaDetalle, ReseñaCreate, ReseñaUpdate, ReseñaDelete


urlpatterns = [
    path('', ReseñaList.as_view(), name='ListaReseñas'),
    path('<int:pk>/detalle/', ReseñaDetalle.as_view(), name='DetalleReseñas'),
    path('crear/', ReseñaCreate.as_view(), name='NuevaReseñas'),
    path('<int:pk>/actualizar/', ReseñaUpdate.as_view(), name='EditReseñas'),
    path('<int:pk>/borrar/', ReseñaDelete.as_view(), name='DeleteReseñas'),
     
]
 