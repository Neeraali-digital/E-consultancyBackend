from rest_framework import serializers
from .models import Application
from students.serializers import StudentSerializer
from courses.serializers import CourseSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    student_id = serializers.IntegerField(write_only=True)
    course_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Application
        fields = ['id', 'student', 'student_id', 'course', 'course_id', 'application_date', 'status', 'remarks', 'created_at', 'updated_at']
        read_only_fields = ['id', 'application_date', 'created_at', 'updated_at']