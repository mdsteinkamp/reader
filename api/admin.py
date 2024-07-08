from django.contrib import admin

from .models import User, Book, Character

class UserAdmin(admin.ModelAdmin):
    list_display = ("username", )

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "date_added")

class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "character_book")

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Character, CharacterAdmin)
