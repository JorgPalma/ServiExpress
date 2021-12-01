from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Fecha(models.Model):
    dia = models.CharField(max_length=30)

    def __str__(self):
        return self.dia

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, null=True)
    precio = models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

opc_hora = [
    [0, "8:00hrs. - 8:59hrs."],
    [1, "9:00hrs. - 9:59hrs."],
    [2, "10:00hrs. - 10:59hrs."],
    [3, "11:00hrs. - 11:59hrs."],
    [4, "12:00hrs. - 12:59hrs."],
    [5, "13:00hrs. - 13:59hrs."],
    [6, "14:00hrs. - 14:59hrs."]
]

class Agendar(models.Model):
    fecha = ForeignKey(Fecha, on_delete=models.PROTECT)
    servicio = ForeignKey(Servicio, on_delete=models.PROTECT)
    hora = models.IntegerField(choices=opc_hora)

    def __str__(self):
        return self.fecha.dia

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario



