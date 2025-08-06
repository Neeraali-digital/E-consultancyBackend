from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('payments/stats/', views.payment_stats, name='payment-stats'),
]