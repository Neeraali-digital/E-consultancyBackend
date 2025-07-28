"""eConsultancy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import dashboard_stats
from .api_root import api_root
from .simple_swagger import swagger_ui, api_schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', swagger_ui, name='swagger-ui'),
    path('api/schema/', api_schema, name='api-schema'),
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
