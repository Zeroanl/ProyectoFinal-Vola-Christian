from django.db import models
from tienda.models import Producto
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.

def validate_to(value):
    if value not in [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]:
        raise ValidationError("Invalid 'to' value.")


class ReseñaClientes (models.Model):
    titulo = models.CharField(max_length=255)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    contenido = models.TextField(blank =True, null=True)
    rating = models.FloatField(null=False,validators=[validate_to])
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Reseña"
        verbose_name_plural="Reseñas"

    def __str__(self):
        return f"-Evaluacion: {self.rating}  -Titulo: {self.titulo} - Producto: {self.producto}"
