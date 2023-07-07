from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home),
    path('registrarCurso/', views.registrarCurso, name='registrar_curso'),
    path('edicionCurso/<codigo>', views.edicionCurso, name='editar_curso'),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>/', views.eliminarCurso, name='eliminar_curso')
     
]
