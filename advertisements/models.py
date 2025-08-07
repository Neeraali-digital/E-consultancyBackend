from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()
    button_text = models.CharField(max_length=100, default='Learn More')
    image = models.ImageField(upload_to='advertisements/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title