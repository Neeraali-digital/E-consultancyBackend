from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationListCreateView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__user__username', 'course__name']

class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

@api_view(['GET'])
def application_stats(request):
    total = Application.objects.count()
    pending = Application.objects.filter(status='pending').count()
    approved = Application.objects.filter(status='approved').count()
    rejected = Application.objects.filter(status='rejected').count()
    cancelled = Application.objects.filter(status='cancelled').count()
    
    return Response({
        'total': total,
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
        'cancelled': cancelled
    })
