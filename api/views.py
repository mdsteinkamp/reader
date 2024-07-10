import json

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from .serializers import UserSerializer, BookSerializer, CharacterSerializer
from .models import User, Book, Character

def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response["X-CSRFToken"] = get_token(request)
    print("csrf token:", response["X-CSRFToken"])
    return response

@require_POST
def login_view(request):
    data = json.loads(request.body)
    print(data)
    print(User.objects.all().first())
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return JsonResponse({'detail': 'Please provide username and password.'}, status=400)
    
    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})

class SessionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'isAuthenticated': True})


class WhoAmIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        return JsonResponse({'username': request.user.username})

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

# class LoginView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': str(request.user),  # `django.contrib.auth.User` instance.
#             'auth': str(request.auth),  # None
#         }
#         return Response(content)  
