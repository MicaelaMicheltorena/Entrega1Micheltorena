from django.urls import path
from .views import formulario_curso, busqueda_curso, formulario_estudiante, formulario_profesor

urlpatterns = [
    path("curso/", formulario_curso, name="formulario_curso"),
    path("estudiante/", formulario_estudiante, name="formulario_estudiante"),
    path("profesor/", formulario_profesor, name="formulario_profesor"),
    path("busqueda-curso/", busqueda_curso, name= "busqueda_curso")
]
