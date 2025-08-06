from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('applications/stats/', views.application_stats, name='application-stats'),
]