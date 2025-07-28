from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .complete_swagger import complete_swagger_ui, complete_api_schema

def api_root(request):
    return HttpResponse("API Root - All endpoints available")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', complete_swagger_ui, name='complete-swagger'),
    path('complete-api-schema/', complete_api_schema, name='complete-api-schema'),
    path('api/', api_root, name='api-root'),
    path('api/', include('users.urls')),
    path('api/', include('students.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('applications.urls')),
    path('api/', include('payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(f"URLs loaded: {len(urlpatterns)} patterns")