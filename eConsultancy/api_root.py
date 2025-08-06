from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list-create', request=request, format=format),
        'students': reverse('student-list-create', request=request, format=format),
        'colleges': reverse('college-list-create', request=request, format=format),
        'courses': reverse('course-list-create', request=request, format=format),
        'applications': reverse('application-list-create', request=request, format=format),
        'payments': reverse('payment-list-create', request=request, format=format),
        'auth': {
            'login': reverse('login', request=request, format=format),
            'register': reverse('register', request=request, format=format),
        },
        'dashboard': reverse('dashboard-stats', request=request, format=format),
    })