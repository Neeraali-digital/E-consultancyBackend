from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentInquiryViewSet

router = DefaultRouter()
router.register(r'', StudentInquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
