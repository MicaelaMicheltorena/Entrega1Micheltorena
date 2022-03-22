from django.contrib import admin

from clase.models import Curso, Entregable, Estudiante, Profesor

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
admin.site.register(Curso)