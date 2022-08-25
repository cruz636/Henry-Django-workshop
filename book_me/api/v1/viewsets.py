from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from book_me.models import *
from book_me.api.v1.serializers import *


class EventosViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    @action(detail=True, methods=["post"], url_path="comprar-vip")
    def comprar_vip(self, request, *args, **kwargs):
        evento = self.get_object()
        if not evento.tiene_vip:
            return Response(
                {
                    "mensaje": "Este evento no posee VIP."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        entrada = Entrada.objects.create(
            evento = evento,
            vip = True,
            email_comprador = request.data.get("email"), # validar con serializers
        )

        entrada.enviar_token()
        print("Enviando entrada por correo electronico")
        return Response(
                {
                    "mensaje": "Su compra se ha realizado con exito!"
                },
                status=status.HTTP_200_OK,
            )

    @action(detail=True, methods=["post"], url_path="comprar-general")
    def comprar_general(self, request, *args, **kwargs):
        evento = self.get_object()
        entrada = Entrada.objects.create(
            evento = evento,
            vip = False,
            email_comprador = request.data.get("email"), # validar con serializers
        )

        entrada.enviar_token()
        print("Enviando entrada por correo electronico")
        return Response(
                {
                    "mensaje": "Su compra se ha realizado con exito!"
                },
                status=status.HTTP_200_OK,
            )

    @action(detail=True, methods=["post"], url_name="comprar")
    def comprar(self, request, *args, **kwargs):
        serializer = ComprarEntradaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        evento = self.get_object()
        entrada = Entrada.objects.create(
            evento = evento,
            vip = serializer.validated_data["vip"],
            email_comprador = serializer.validated_data["email"],
        )
        entrada.enviar_token()
        tipo = "VIP" if serializer.validated_data["vip"] else "GENERAL"
        print("Enviando entrada por correo electronico")
        return Response(
                {
                    "mensaje": f"Has comprado una entrada {tipo} para {evento}"
                },
                status=status.HTTP_200_OK,
            )
    

class ArtistasViewSet(viewsets.ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

