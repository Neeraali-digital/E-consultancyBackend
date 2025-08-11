from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from .swagger_views import swagger_ui, api_schema

def api_root(request):
    return JsonResponse({
        'message': 'E-Consultancy Backend API - Complete Version',
        'status': 'working',
        'version': '1.0.0',
        'documentation': '/swagger/',
        'endpoints': {
            'swagger': '/swagger/',
            'admin': '/admin/',
            'users': '/api/users/',
            'students': '/api/students/',
            'courses': '/api/courses/',
            'colleges': '/api/colleges/',
            'applications': '/api/applications/',
            'payments': '/api/payments/',
            'advertisements': '/api/advertisements/',
            'auth': '/api/auth/'
        }
    })

urlpatterns = [
    path('', api_root, name='home'),
    path('swagger/', swagger_ui, name='swagger-ui'),
    path('api-schema/', api_schema, name='api-schema'),
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('users.urls')),
    path('api/', include('students.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('applications.urls')),
    path('api/', include('payments.urls')),
    path('api/', include('advertisements.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(f"URLs loaded: {len(urlpatterns)} patterns")