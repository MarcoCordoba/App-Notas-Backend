from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tareas/', include('tareas.urls')),
    path('api/auth/', include('login.urls')),  # <- esta línea es clave
]
