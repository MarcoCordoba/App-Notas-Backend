from rest_framework import serializers 
from .models import tarea


class tareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tarea
        fields = '__all__'
        read_only_fields = ['usuario']

