from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Role
from students.models import Student
from courses.models import Course, College, Blog, Review
from applications.models import Application
from payments.models import Payment
from datetime import date, datetime
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for the e-consultancy system'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create roles
        admin_role, _ = Role.objects.get_or_create(name='Admin', defaults={'description': 'System Administrator'})
        student_role, _ = Role.objects.get_or_create(name='Student', defaults={'description': 'Student User'})
        
        # Create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'role': admin_role,
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
        
        # Create sample colleges
        colleges_data = [
            {
                'name': 'Indian Institute of Technology Delhi',
                'location': 'New Delhi, Delhi',
                'type': 'engineering',
                'established': 1961,
                'rating': Decimal('4.8'),
                'description': 'Premier engineering institute known for excellence in technology and research.',
                'website': 'https://www.iitd.ac.in',
                'email': 'info@iitd.ac.in',
                'phone': '9876543210'
            },
            {
                'name': 'All India Institute of Medical Sciences',
                'location': 'New Delhi, Delhi',
                'type': 'medical',
                'established': 1956,
                'rating': Decimal('4.9'),
                'description': 'Leading medical institute providing quality healthcare education.',
                'website': 'https://www.aiims.edu',
                'email': 'info@aiims.edu',
                'phone': '9876543211'
            }
        ]
        
        for college_data in colleges_data:
            College.objects.get_or_create(name=college_data['name'], defaults=college_data)
        
        # Create sample courses
        iit_delhi = College.objects.get(name='Indian Institute of Technology Delhi')
        aiims = College.objects.get(name='All India Institute of Medical Sciences')
        
        courses_data = [
            {
                'name': 'Bachelor of Technology in Computer Science',
                'code': 'CSE101',
                'category': 'engineering',
                'duration': '4 Years',
                'degree_type': 'undergraduate',
                'description': 'Comprehensive program covering computer science fundamentals.',
                'eligibility': '10+2 with PCM and minimum 60% marks',
                'annual_fee': Decimal('150000'),
                'total_fee': Decimal('600000'),
                'college': iit_delhi
            },
            {
                'name': 'Bachelor of Medicine and Bachelor of Surgery',
                'code': 'MBBS101',
                'category': 'medical',
                'duration': '5.5 Years',
                'degree_type': 'undergraduate',
                'description': 'Comprehensive medical education program.',
                'eligibility': '10+2 with PCB and NEET qualification',
                'annual_fee': Decimal('500000'),
                'total_fee': Decimal('2750000'),
                'college': aiims
            }
        ]
        
        for course_data in courses_data:
            Course.objects.get_or_create(code=course_data['code'], defaults=course_data)
        
        # Create sample student users
        student_users_data = [
            {
                'username': 'john_doe',
                'email': 'john@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'role': student_role
            },
            {
                'username': 'jane_smith',
                'email': 'jane@example.com',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'role': student_role
            }
        ]
        
        for user_data in student_users_data:
            user, created = User.objects.get_or_create(username=user_data['username'], defaults=user_data)
            if created:
                user.set_password('password123')
                user.save()
                
                # Create student profile
                Student.objects.get_or_create(
                    user=user,
                    defaults={
                        'date_of_birth': date(2000, 1, 1),
                        'nationality': 'Indian',
                        'guardian_name': f"{user.first_name}'s Guardian",
                        'guardian_contact': '9876543210'
                    }
                )
        
        # Create sample blog
        Blog.objects.get_or_create(
            title='Welcome to Our E-Consultancy Platform',
            defaults={
                'slug': 'welcome-to-our-platform',
                'content': 'This is a sample blog post about our e-consultancy platform.',
                'excerpt': 'Welcome to our educational consultancy platform.',
                'status': 'published',
                'author': admin_user
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))