from django.http import HttpResponse
from django.shortcuts import render
from .models import Tutorx, Mascota, atencionprofesional
from django.template import loader
from entregalucero.forms import tutorxsFormulario, mascotasFormulario, atencionprofesionalFormulario

# Create your views here.

def inicio (request):
    inicio = loader.gettemplate('inicio.html')
    return render (request, 'inicio.html', {inicio: inicio})
    
def tutorxs (request):
    tutorxs_vet_list = Tutorx.objects.all()
    return render (request,'tutorxs.html', {'tutorxs': tutorxs_vet_list})

def mascotas(request):
    mismascotas_list = Mascota.objects.all()
    return render (request, 'mascotas.html' , {'mascotas': mismascotas_list}) 

def atencion_profesional (request):
    miatencion_list = atencionprofesional.objects.all()
    return render (request, 'atencion_profesional.html', { 'atencion_profesional' : miatencion_list})

def tutorxs (request):
    return render (request,'entregalucero/tutorxs.html') 

def mascotas(request):
    return render (request, 'entregalucero/mascotas.html')

def atencion_profesional (request):
    return render (request, 'entregalucero/atencion_profesional.html')

def inicio (request):
    return render (request, 'entregalucero/inicio.html')

def miveteFormulario(request):
    if request.method == 'POST':
      miFormulario =  tutorxsFormulario(request.POST) 
      if miFormulario.is_valid():
        informacion = miFormulario.cleaned_data
      nombre = informacion ['tutorxs'] 
      apellido = informacion ['tutorxs'] 
      nombre_mascota = informacion ['tutorxs']
      tutorxs = Tutorx (nombre=nombre, apellido=apellido, nombre_mascota = nombre_mascota)
      tutorxs.save()
      return render (request, 'entregalucero/inicio.html')
    else:
        miFormulario = tutorxsFormulario()
        return render (request, 'entregalucero/miveteFormulario.html', {'miFormulario': miFormulario })


def mascotasformulario (request):
    if request.method == 'POST':
      miFormulario =  mascotasFormulario(request.POST) 
      if miFormulario.is_valid():
        informacion = miFormulario.cleaned_data
      nombre = informacion ['nombre'] 
      nombre_tutorx = informacion ['nombre_tutorx'] 
      especie = informacion ['especie']
      raza = informacion ['raza']
      vacunas = informacion ['vacunas']
      edad = informacion ['edad']
      peso = informacion ['peso']
      mascotas = Mascota (nombre=nombre, nombre_tutorx = nombre_tutorx , especie = especie, raza = raza, vacunas = vacunas, edad = edad, peso = peso)
      mascotas.save()
      return render (request, 'entregalucero/inicio.html')
    else:
        miFormulario = mascotasFormulario()
        return render (request, 'entregalucero/mascotasFormulario.html', {'miFormulario': miFormulario })

def atencion_profesionalForm (request):
    if request.method == 'POST':
      miFormulario =  atencionprofesionalFormulario(request.POST) 
      if miFormulario.is_valid():
        informacion = miFormulario.cleaned_data
      nombre_profesional= informacion ['nombre_profesional']
      motivo_de_atencion = informacion ['motivo_de_atencion']
      proxima_visita = ['proxima_visita']
      atencion_prof = atencionprofesional (nombre_profesional = nombre_profesional, motivo_de_atencion = motivo_de_atencion,  proxima_visita = proxima_visita, )
      atencion_prof.save()
      return render (request, 'entregalucero/inicio.html')
    else:
        miFormulario = atencionprofesionalFormulario
        return render (request, 'entregalucero/atencionprofesionalFormulario.html', {'miFormulario': miFormulario })
    
def busquedatutorx (request):
  return render (request, 'entregalucero/busquedatutorx.html')

def buscar(request):
    if request.GET ['tutorxs']:
        nombre_mascota = request.GET ['tutorxs']
        nombre = Tutorx.objects.filter(tutorxs = tutorxs)
        return render (request, 'entregalucero/resultadosBusqueda.html', {'nombre': nombre, 'nombre_mascota': nombre_mascota})
    else:
        respuesta= "no se ha ingresado ningun dato"
    return HttpResponse(respuesta)
    
# respuesta= f"Estoy buscando el nombre del tutorx {request.GET['tutorx']}"