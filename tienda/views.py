from django.shortcuts import render,redirect
from .models import Producto,CategoriaProd



# Create your views here.

def tienda(request):
    productos=Producto.objects.all()
    return render(request,"tienda/tienda.html",{"productos":productos})

def categoria(request, categoriaProd_id):
    categoria=CategoriaProd.objects.get(id=categoriaProd_id)
    productos=Producto.objects.filter(categorias=categoria)
    return render(request, "tienda/categoriasProd.html", {"categoria":categoria,"productos":productos})

def busqueda_productos(request):
    return render(request, "tienda/busqueda.html")

def buscar(request):
    if request.GET["prd"]:
        producto=request.GET["prd"]
        articulos=Producto.objects.filter(nombre__icontains=producto)
        return render(request, "tienda/resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else:
        return redirect("Tienda")
    
def agradecimiento(request):
    return render(request,"tienda/agradecimientoCompras.html")


def detalles_productos(request, producto_id):
    producto = Producto.objects.filter(id=producto_id)
    return render(request, 'tienda/detalle.html', {'productos': producto} )


