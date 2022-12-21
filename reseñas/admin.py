from django.contrib import admin
from .models import ReseñaClientes

# Register your models here.

class ReseñaAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(ReseñaClientes, ReseñaAdmin)