

from django.db import models

class College(models.Model):
    TYPE_CHOICES = [
        ('engineering', 'Engineering'),
        ('medical', 'Medical'),
        ('management', 'Management'),
        ('arts', 'Arts'),
        ('law', 'Law'),
        ('pharmacy', 'Pharmacy'),
    ]
    INSTITUTION_TYPE_CHOICES = [
        ('government', 'Government'),
        ('private', 'Private'),
        ('deemed', 'Deemed'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    established = models.PositiveIntegerField()
    ranking = models.PositiveIntegerField(null=True, blank=True)
    institution_type = models.CharField(max_length=20, choices=INSTITUTION_TYPE_CHOICES, blank=True)
    affiliated = models.CharField(max_length=200, blank=True)
    courses = models.JSONField(default=list, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='colleges/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('engineering', 'Engineering'),
        ('medical', 'Medical'),
        ('management', 'Management'),
        ('arts', 'Arts'),
        ('law', 'Law'),
        ('pharmacy', 'Pharmacy'),
    ]
    DEGREE_CHOICES = [
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate'),
        ('diploma', 'Diploma'),
        ('certificate', 'Certificate'),
        ('doctorate', 'Doctorate'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    duration = models.CharField(max_length=50)
    degree_type = models.CharField(max_length=20, choices=DEGREE_CHOICES)
    description = models.TextField(blank=True)
    eligibility = models.TextField(blank=True)
    # Fee fields removed
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='course_list', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    featured_image = models.ImageField(upload_to='blogs/', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='reviews')
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.rating} stars"
