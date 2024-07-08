from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, BookSerializer, CharacterSerializer
from .models import User, Book, Character

class UserView(viewsets.ModelViewSet):
    serializer_class: UserSerializer
    queryset = User.objects.all()

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CharacterView(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()