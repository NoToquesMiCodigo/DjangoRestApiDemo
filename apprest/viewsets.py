from .models import Libro, Autor
from .serializers import LibroSerializer, AutorSerializer
from rest_framework import viewsets

class LibroViewSet(viewsets.ModelViewSet):
	
    serializer_class = LibroSerializer
    queryset = Libro.objects.all()

class AutorViewSet(viewsets.ModelViewSet):
	
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()
