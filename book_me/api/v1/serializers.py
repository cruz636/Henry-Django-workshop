from rest_framework import serializers

from book_me.models import *


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = [
            "nombre",
            "estilo",
            "precio_de_contratacion"
        ]


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = [ 
            "nombre",
            "artista",
            "lugar",
            "fecha",
            "tiene_vip",
            "capacidad_general",
            "capacidad_sector_vip",
            "precio_entrada_general",
            "precio_entrada_vip",
        ]


class EntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrada
        fields = [ 
            "evento",
            "vip",
            "email_comprador"
        ]


class ComprarEntradaSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    vip = serializers.BooleanField(required=True)