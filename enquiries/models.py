from django.db import models

class StudentInquiry(models.Model):
    INQUIRY_TYPES = (
        ('standard', 'Standard'),
        ('quick', 'Quick'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15)
    course_of_interest = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES, default='standard')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course_of_interest} ({self.inquiry_type})"

    class Meta:
        verbose_name_plural = "Student Inquiries"
        ordering = ['-created_at']
