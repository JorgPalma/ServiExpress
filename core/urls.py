from django import urls
from django.urls import path
from .views import home, agendar, agregar_servicio, listar_servicio, editar_servicio, eliminar_servicio, registro, listar_hora, listar_usuario

urlpatterns = [
    path('', home, name="home"),
    path('agendar/', agendar, name="agendar"),
    path('agregar_servicio/', agregar_servicio, name="agregar_servicio"),
    path('listar_servicio/', listar_servicio, name="listar_servicio"),
    path('editar_servicio/<id>/', editar_servicio, name="editar_servicio"),
    path('eliminar_servicio/<id>/', eliminar_servicio, name="eliminar_servicio"),
    path('registro/', registro, name="registro"),
    path('listar_hora/', listar_hora, name="listar_hora"),
    path('listar_usuario', listar_usuario, name="listar_usuario")
]