

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_months = models.PositiveIntegerField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
