# tours/views.py

from django.shortcuts import render

def login(request):
    return render(request, 'tours/login.html')

def home_ejecutivo(request):
    return render(request, 'tours/home_ejecutivo.html')

def crear_curso(request):
    return render(request, 'tours/crear_curso.html')

def ver_cursos(request):
    return render(request, 'tours/ver_cursos.html')

def home_apoderado(request):
    return render(request, 'tours/home_apoderado.html')

def informacion_pagos(request):
    return render(request, 'tours/informacion_pagos.html')

def perfil_apoderado(request):
    return render(request, 'tours/perfil_apoderado.html')

def realizar_pago(request):
    return render(request, 'tours/realizar_pago.html')

