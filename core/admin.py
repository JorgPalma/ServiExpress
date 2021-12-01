from django.contrib import admin
from .models import Fecha, Servicio, Usuario, Agendar

# Register your models here.

admin.site.register(Fecha)
admin.site.register(Servicio)
admin.site.register(Agendar)
admin.site.register(Usuario)