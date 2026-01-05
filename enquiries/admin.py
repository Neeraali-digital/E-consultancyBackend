from django.contrib import admin
from .models import StudentInquiry

@admin.register(StudentInquiry)
class StudentInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'course_of_interest', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
