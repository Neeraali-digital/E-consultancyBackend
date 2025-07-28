from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Test works!")

def swagger_view(request):
    return HttpResponse("Swagger works!")

def redoc_view(request):
    return HttpResponse("ReDoc works!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('swagger/', swagger_view),
    path('redoc/', redoc_view),
]