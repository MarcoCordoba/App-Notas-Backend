from rest_framework import serializers 
from .models import tarea


class tareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields = '__all__'

