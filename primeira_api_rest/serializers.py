# Criar este arquivo
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User            # Modelo a ser serializado pra json
        fields = '__all__'      # Campos do modelo a serem serializados
