from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
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

# def loginview(request):
#     if request.method == "POST":
#         user = authenticate(request, username=request.POST["username"])

#     if user:
#         login(request, user)
#         messages.success(request, "Logged in Successfully")
#         return redirect('/')
#     else: 
#         messages.error(request, 'Loggin in Fail')
#     return render(request, '/')

class LoginView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)  
