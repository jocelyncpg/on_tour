# on_tour/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración de Django
    path('', include('tours.urls')),  # Incluye las URLs de la aplicación 'tours'
]
