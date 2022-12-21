# Proyecto Final Curso Python CoderHouse
- Alumno: Vola Christian
- Tematica: Tienda de Hardware
- Este proyecto fue probado con python 3.10.7 y Django 4.1.4


## Archivos necesarios


### PYTHON
Para comenzar primero tienen que asegurarse que tienen instalado, python.
En windows tiene que abrir una terminal cmd o powershell.
```
PS C:\> python --version
Python 3.X.X 
```
En Linux/Mac tiene que abrir una terminal bash
```
$ python --version
Python 3.X.X 
```
Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este [Link](https://www.python.org/downloads/)


### DJANGO
En una terminal cmd o powershell desde windows:
```
C:\> pip install django
```
Linux/Mac:
```
$ pip install django
```
Si no arrojo errores esto es suficiente para poder correr el projecto.


### DJANGO BOOTSTRAP V5
En una terminal cmd o powershell desde windows:
```
C:\> pip install django-bootstrap-v5
```
Linux/Mac:
```
$ pip install django-bootstrap-v5
```


### DJANGO CRISPY FORMS
En una terminal cmd o powershell desde windows:
```
C:\> pip install django-crispy-forms
```
Linux/Mac:
```
$ pip install django-crispy-forms
```


## Configuracion Email
En el archivo ProyectoFinal/settings.py (linea 152 y 153) editar:
```
EMAIL_ HOST_USER = 'colocar mail tienda'
EMAIL_HOST_PASSWORD = 'password'
```
- Preferentemente un GMAIL ya que debemos generar una contraseña de aplicacion, es el mail que utilizara la tienda
- El password que debe ser generada desde el panel de seguridad de Google, Contraseñas de aplicaciones

En el archivo pedidos/views.py, en la funcion  "enviar_mail" (linea 50) editar:
```
from_email = "colocar mail tienda"
```

En el archivo contacto/views.py en la funcion "contacto" (linea 18) editar el 'colocar mail tienda' :
```
'El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n  {}' .format(nombre,email,mensaje),'',['colocar mail tienda'],'', reply_to=[email] )
```

Esto permite a la pagina poder enviar emails a los clientes con sus pedidos y recibir mails de la app contactos de la pagina


## Correr el Servidor
Los siguientes comandos son analogos en Mac/Linux/Windows:
```
cd 'direccion carpeta contenedora'
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.
Luego arrancamos el servidor web
```
python manage.py runserver
```
Ahora Hace click en el siguiente link para ver el ejemplo corriendo: 
[http://localhost:8000/](http://localhost:8000/)


## Casos de Prueba
Planilla de casos de prueba :  [Link](https://docs.google.com/spreadsheets/d/1XySA5ugwOrrtHWxjiakMzrzg_ksIzNjc8GoKzfCa-EE/edit?usp=sharing)


## Video
Video de Youtube explicando las funcionalidades de la pagina : [Link](https://www.youtube.com/watch?v=0Sty0q9RpVk)
