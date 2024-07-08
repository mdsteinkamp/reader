from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    character_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

