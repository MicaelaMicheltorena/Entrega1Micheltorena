from django.shortcuts import render
from clase.models import Curso, Estudiante, Profesor
from clase.forms import Busquedacurso, Cursoformulario, Estudianteformulario, Profesorformulario
# Create your views here.

def formulario_curso(request):
  if request.method == "POST":
    formulario = Cursoformulario(request.POST)
    
    if formulario.is_valid():
      data = formulario.cleaned_data
      nuevo_curso = Curso(nombre = data["curso"], camada = data["camada"])
      nuevo_curso.save()
      return render(request, "indice/index.html" , {"nuevo_curso": nuevo_curso})
    
  formulario = Cursoformulario()
  return render(request, "clase/formulario_curso.html" , {"formulario": formulario})

def formulario_estudiante(request):
  if request.method == "POST":
    formulario = Estudianteformulario(request.POST)
    
    if formulario.is_valid():
      data = formulario.cleaned_data
      nuevo_estudiante = Estudiante(nombre = data["nombre"], apellido = data["apellido"], email = data["email"])
      nuevo_estudiante.save()
      return render(request, "indice/index.html" , {"nuevo_estudiante": nuevo_estudiante})
    
  formulario = Estudianteformulario()
  return render(request, "clase/formulario_estudiante.html" , {"formulario": formulario})

def formulario_profesor(request):
  if request.method == "POST":
    formulario = Profesorformulario(request.POST)
    
    if formulario.is_valid():
      data = formulario.cleaned_data
      nuevo_profesor = Profesor(nombre = data["nombre"], apellido = data["apellido"], email = data["email"], profesion = data["profesion"])
      nuevo_profesor.save()
      return render(request, "indice/index.html" , {"nuevo_profesor": nuevo_profesor})
    
  formulario = Profesorformulario()
  return render(request, "clase/formulario_profesor.html" , {"formulario": formulario})

def busqueda_curso(request):
  
  dato = request.GET.get("partial_curso", None)
  buscador = Busquedacurso()
  if dato is not None:
    cursos_buscados = Curso.objects.filter(nombre__icontains=dato) 
    return render(request, "clase/busqueda_curso.html", {"buscador": buscador, "cursos_buscados": cursos_buscados, "dato": dato})
  
  return render(request, "clase/busqueda_curso.html", 
                {"buscador": buscador, "dato": dato})
