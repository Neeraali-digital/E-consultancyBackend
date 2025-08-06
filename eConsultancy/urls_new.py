from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def swagger_view(request):
    return HttpResponse("Swagger UI works!")

def redoc_view(request):
    return HttpResponse("ReDoc works!")

from .views import dashboard_stats
from .api_root import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger_view, name='swagger-ui'),
    path('redoc/', redoc_view, name='redoc-ui'),
    path('api/', api_root, name='api-root'),
    path('api/dashboard/stats/', dashboard_stats, name='dashboard-stats'),
    path('api/', include('users.urls')),
    path('api/', include('students.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('applications.urls')),
    path('api/', include('payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)