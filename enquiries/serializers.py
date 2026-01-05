from rest_framework import serializers
from .models import StudentInquiry

class StudentInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInquiry
        fields = '__all__'
