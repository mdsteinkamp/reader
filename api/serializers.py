from rest_framework import serializers

from .models import User, Book, Character

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username")

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title")
        user = ("user")

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "name", "character_book")