from django.http import HttpResponse
from django.shortcuts import render
from .models import Tutorx, Mascota, atencionprofesional
from django.template import loader

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