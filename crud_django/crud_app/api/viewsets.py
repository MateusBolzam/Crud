# No arquivo crud_app/api/viewsets.py

from rest_framework import generics
from ..models import classe, personagem  # Ajuste o nome da classe do modelo
from .serializers import ClasseSerializer, PersonagemSerializer


# Class API
class ClasseListCreateView(generics.ListCreateAPIView):
    queryset = classe.objects.all()
    serializer_class = ClasseSerializer

class ClasseRetrieveView(generics.RetrieveAPIView):
    queryset = classe.objects.all()
    serializer_class = ClasseSerializer

class ClasseUpdateView(generics.UpdateAPIView):
    queryset = classe.objects.all()
    serializer_class = ClasseSerializer

class ClasseDestroyView(generics.DestroyAPIView):
    queryset = classe.objects.all()
    serializer_class = ClasseSerializer


# Personagem API
class PersonagemListCreateView(generics.ListCreateAPIView):
    queryset = personagem.objects.all()
    serializer_class = PersonagemSerializer

class PersonagemRetrieveView(generics.RetrieveAPIView):
    queryset = personagem.objects.all()
    serializer_class = PersonagemSerializer

class PersonagemUpdateView(generics.UpdateAPIView):
    queryset = personagem.objects.all()
    serializer_class = PersonagemSerializer

class PersonagemDestroyView(generics.DestroyAPIView):
    queryset = personagem.objects.all()
    serializer_class = PersonagemSerializer
