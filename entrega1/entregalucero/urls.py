
from django.urls import path
from entregalucero import views 
from entregalucero.views import tutorxs, mascotas, atencion_profesional, inicio, miveteFormulario, mascotasformulario, atencion_profesionalForm, busquedatutorx, buscar


urlpatterns = [
    path('tutorxs/', tutorxs, name = 'Tutorxs'),
    path ('mascotas/', mascotas, name = 'Mascotas'),
    path ('atencion_profesional/', atencion_profesional, name = 'Atencion_profesional'), 
    path ('inicio/', inicio, name = 'Inicio'), 
    path  ('miveteFormulario/', miveteFormulario, name = 'miveteFormulario'),
    path  ('mascotasformulario/', mascotasformulario, name = 'mascotasFormulario'),
    path ('atencion_profesionalForm/', atencion_profesionalForm, name = 'atencionprofesionalFormulario'),
    path ('busquedatutorx/', busquedatutorx, name = 'busquedatutorx'),
    path ('buscar/', buscar, name='buscar'), 
]
