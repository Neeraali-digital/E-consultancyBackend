from rest_framework import serializers
from .models import Student
from users.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'user', 'user_id', 'date_of_birth', 'nationality', 'guardian_name', 'guardian_contact', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user_id', 'date_of_birth', 'nationality', 'guardian_name', 'guardian_contact']