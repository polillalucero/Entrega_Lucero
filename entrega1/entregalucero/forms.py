from django import forms

class tutorxsFormulario(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Apellido = forms.CharField(max_length=50)
    Ocupacion = forms.CharField(max_length=50)
    Edad = forms.IntegerField()
    nombre_mascota = forms.CharField(max_length=50)


class mascotasFormulario(forms.Form):
    Nombre = forms.CharField(max_length=50)
    Nombre_tutorx = forms.CharField(max_length=50)
    Especie = forms.CharField(max_length=50)
    Raza = forms.CharField(max_length=50)
    Vacunas = forms.CharField(max_length=50)
    Edad = forms.IntegerField()
    Peso = forms.IntegerField()

class atencionprofesionalFormulario(forms.Form):
     Nombre_profesional= forms.CharField(max_length=50)
     Motivo_de_atencion = forms.CharField(max_length=200)
     Proxima_visita = forms.DateField()
