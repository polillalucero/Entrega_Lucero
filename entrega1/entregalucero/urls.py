
from django.urls import path
from entregalucero import views 
from entregalucero.views import tutorxs, mascotas, atencion_profesional, inicio

urlpatterns = [
    path('tutorxs/', tutorxs, name = 'Tutorxs'),
    path ('mascotas/', mascotas, name = 'Mascotas'),
    path ('atencion_profesional/', atencion_profesional, name = 'Atencion_profesional'), 
    path ('inicio', inicio, name = 'Inicio'), 
]
