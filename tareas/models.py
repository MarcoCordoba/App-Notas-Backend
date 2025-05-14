from django.db import models

# Create your models here.
class tarea(models.Model):
    
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True) #esta caracteristica dice que el campo puede estar vacio
    hecho = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
