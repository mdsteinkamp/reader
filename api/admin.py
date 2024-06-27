from django.contrib import admin

from .models import Book, Character

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")

class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "character_book")

admin.site.register(Book, BookAdmin)
admin.site.register(Character, CharacterAdmin)
