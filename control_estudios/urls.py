from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_estudiantes, listar_cursos

urlpatterns = [
    path("estudiantes/", listar_estudiantes, name="lista_estudiantes"),
    path("cursos/", listar_cursos, name= "lista_cursos"),
]
