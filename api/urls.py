from django.urls import path
from . import views
from rest_framework import routers


from . import views

app_name = "reader"
router = routers.DefaultRouter()
router.register('users', views.UserView, 'user')
router.register('books', views.BookView, 'book')
router.register('characters', views.CharacterView, 'character')


urlpatterns = [
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', views.SessionView.as_view(), name='api-session'),
    path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),
]