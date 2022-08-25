from secrets import token_urlsafe
from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=255)
    estilo = models.CharField(max_length=255)
    precio_de_contratacion = models.FloatField()

    def __str__(self) -> str:
        return self.nombre 


class Lugar(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre    


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    artista = models.ForeignKey(
        Artista, 
        on_delete=models.CASCADE,
        related_name="eventos",
        )
    lugar = models.OneToOneField(
        Lugar,
        null=True,
        on_delete=models.SET_NULL, 
        )
    fecha = models.DateField()
    tiene_vip = models.BooleanField(default=False)
    capacidad_general = models.IntegerField()
    capacidad_sector_vip = models.IntegerField(default=0)
    entradas_general_vendidas = models.IntegerField(default=0)
    entradas_vip_vendidas = models.IntegerField(default=0)
    precio_entrada_general = models.FloatField()
    precio_entrada_vip = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.nombre 


class Entrada(models.Model):
    evento = models.ForeignKey(
        Evento, 
        on_delete=models.CASCADE, 
        related_name="entradas_vendidas",
        )
    vip = models.BooleanField()
    email_comprador = models.EmailField()
    secure_token = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.evento} | {self.email_comprador}"

    def precio(self):
        if self.vip:
            return self.evento.precio_entrada_vip
        else:
            return self.evento.precio_entrada_general

    def enviar_token(self):
        if not self.secure_token:
            self.secure_token = token_urlsafe(60)
            self.save(update_fields=["secure_token"])

        return self.secure_token
