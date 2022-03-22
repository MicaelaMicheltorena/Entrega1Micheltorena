from django import forms

class Cursoformulario(forms.Form):
  curso = forms.CharField(max_length=20)
  camada = forms.IntegerField()
  
class Estudianteformulario(forms.Form):
  nombre = forms.CharField(max_length=20)
  apellido = forms.CharField(max_length=20)
  email = forms.EmailField()
 
class Profesorformulario(forms.Form):
  nombre = forms.CharField(max_length=20)
  apellido = forms.CharField(max_length=20)
  email = forms.EmailField()
  profesion = forms.CharField(max_length=20)

class Entregableformulario(forms.Form):
  nombre = forms.CharField(max_length=20)
  fecha_de_entrega = forms.DateField(input_formats= '%d/%m/%y')
  entregado = forms.BooleanField()

class Busquedacurso(forms.Form):
  partial_curso = forms.CharField(label = "Buscador", max_length=20)
