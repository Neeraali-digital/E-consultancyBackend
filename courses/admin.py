from django.contrib import admin
from .models import Course, College, Blog, Review

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'type', 'established', 'rating', 'status']
    list_filter = ['type', 'status', 'established']
    search_fields = ['name', 'location']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'category', 'degree_type', 'status']
    list_filter = ['category', 'degree_type', 'status']
    search_fields = ['name', 'code']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'student', 'rating', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_approved', 'created_at']
    search_fields = ['title', 'content']
