from rest_framework import serializers

from .models import Book, Character

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title")

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "name", "character_book")