from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'status', 'application_date']
    list_filter = ['status', 'application_date']
    search_fields = ['student__user__username', 'course__name']
