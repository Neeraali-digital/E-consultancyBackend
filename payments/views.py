from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['transaction_id', 'application__student__user__username']

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

@api_view(['GET'])
def payment_stats(request):
    total_payments = Payment.objects.count()
    total_amount = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    pending_payments = Payment.objects.filter(status='pending').count()
    completed_payments = Payment.objects.filter(status='completed').count()
    
    return Response({
        'total_payments': total_payments,
        'total_amount': float(total_amount),
        'pending': pending_payments,
        'completed': completed_payments
    })
