from rest_framework import viewsets
from .models import tarea
from .serializer import tareaSerializer

class tareaView(viewsets.ModelViewSet):
    serializer_class = tareaSerializer
    queryset = tarea.objects.all()
    