
from django.urls import path
from entregalucero import views 
from entregalucero.views import entregalucero, mismascotas, miatencion

urlpatterns = [
    path('entregalucero/', entregalucero),
    path ('mascotas/', mismascotas),
    path ('atencionprofesional/', miatencion), 
]
