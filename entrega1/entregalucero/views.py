from django.http import HttpResponse
from django.shortcuts import render
from .models import Tutorx, Mascota, atencionprofesional

# Create your views here.
def entregalucero(request):
    entrega_vet_list = Tutorx.objects.all()
    return render (request,'entregalucero.html', {'entregalucero': entrega_vet_list})

def mismascotas(request):
    mismascotas_list = Mascota.objects.all()
    return render (request, 'mascotas.html' , {'mascotas': mismascotas_list}) 

def miatencion(request):
    miatencion_list = atencionprofesional.objects.all()
    return render (request, 'atencionprofesional.html', { 'atencionprofesional' : miatencion_list})


