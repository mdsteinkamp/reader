from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # new
]