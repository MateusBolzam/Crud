from ..models import classe,personagem
from rest_framework import serializers


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = classe
        fields = "__all__"
        
class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = personagem
        fields = "__all__"
