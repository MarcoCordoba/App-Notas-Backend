from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import tarea
from .serializer import tareaSerializer

class tareaView(viewsets.ModelViewSet):
    serializer_class = tareaSerializer
    permission_classes = [IsAuthenticated]  # ✅ solo usuarios autenticados

    def get_queryset(self):
        # ✅ Filtra las tareas del usuario autenticado
        return tarea.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        # ✅ Asigna el usuario automáticamente al crear la tarea
        serializer.save(usuario=self.request.user)
