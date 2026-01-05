from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from students.models import Student
from courses.models import Course, College
from applications.models import Application
from payments.models import Payment
from enquiries.models import StudentInquiry
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    """Get overall dashboard statistics"""
    
    now = timezone.now()
    month_ago = now - timedelta(days=30)
    
    stats = {
        'users': {
            'total': User.objects.count(),
            'active': User.objects.filter(is_active=True).count(),
        },
        'students': {
            'total': Student.objects.count(),
        },
        'colleges': {
            'total': College.objects.count(),
            'active': College.objects.filter(status='active').count(),
        },
        'courses': {
            'total': Course.objects.count(),
            'active': Course.objects.filter(status='active').count(),
        },
        'applications': {
            'total': Application.objects.count(),
            'pending': Application.objects.filter(status='pending').count(),
            'approved': Application.objects.filter(status='approved').count(),
        },
        'inquiries': {
            'total': StudentInquiry.objects.count(),
            'today': StudentInquiry.objects.filter(created_at__date=now.date()).count(),
        },
        'payments': {
            'total': Payment.objects.count(),
            'total_amount': float(Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0),
        }
    }
    
    return Response(stats)