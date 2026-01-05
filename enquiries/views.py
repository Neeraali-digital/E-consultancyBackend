from rest_framework import viewsets, permissions
from .models import StudentInquiry
from .serializers import StudentInquirySerializer

class StudentInquiryViewSet(viewsets.ModelViewSet):
    queryset = StudentInquiry.objects.all()
    serializer_class = StudentInquirySerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = StudentInquiry.objects.all()
        inquiry_type = self.request.query_params.get('type', None)
        if inquiry_type:
            queryset = queryset.filter(inquiry_type=inquiry_type)
        return queryset
