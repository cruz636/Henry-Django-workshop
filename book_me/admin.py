from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "fecha"]
    search_fields = ["nombre"]


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    list_display = ["nombre"]


@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ["evento", "email_comprador"]
