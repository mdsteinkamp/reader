from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, CharacterSerializer
from .models import Book, Character

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()