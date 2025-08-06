from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'nationality', 'guardian_name', 'created_at']
    list_filter = ['nationality', 'created_at']
    search_fields = ['user__username', 'user__email', 'guardian_name']
