# tours/urls.py

from django.urls import path
from . import views  # Importa las vistas de la aplicación

urlpatterns = [
    path('login/', views.login, name='login'),  # Ruta para la página de login
    path('home_ejecutivo/', views.home_ejecutivo, name='home_ejecutivo'),  # Ruta para la página de home ejecutivo
    path('crear_curso/', views.crear_curso, name='crear_curso'),  # Ruta para crear curso
    path('ver_cursos/', views.ver_cursos, name='ver_cursos'),  # Ruta para ver cursos
    path('home_apoderado/', views.home_apoderado, name='home_apoderado'),  # Ruta para home apoderado
    path('informacion_pagos/', views.informacion_pagos, name='informacion_pagos'),  # Ruta para información de pagos
    path('perfil_apoderado/', views.perfil_apoderado, name='perfil_apoderado'),  # Ruta para perfil apoderado
    path('realizar_pago/', views.realizar_pago, name='realizar_pago'),  # Ruta para realizar pagos
]
