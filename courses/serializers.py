from rest_framework import serializers
from .models import Course, College, Blog, Review

class CollegeSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = College
        fields = ['id', 'name', 'short_name', 'location', 'type', 'established', 'ranking', 'institution_type', 'affiliated', 'courses', 'rating', 'status', 'description', 'website', 'email', 'phone', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    college = CollegeSerializer(read_only=True)
    college_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'category', 'duration', 'degree_type', 'description', 'eligibility', 'status', 'college', 'college_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'featured_image', 'status', 'author', 'author_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ReviewSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    student_id = serializers.IntegerField(write_only=True)
    college = CollegeSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    college_id = serializers.IntegerField(write_only=True, required=False)
    course_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Review
        fields = ['id', 'student', 'student_id', 'college', 'college_id', 'course', 'course_id', 'rating', 'title', 'content', 'is_approved', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']