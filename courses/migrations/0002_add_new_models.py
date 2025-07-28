# Generated manually to add new models and update Course model

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0002_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        # Create College model
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('engineering', 'Engineering'), ('medical', 'Medical'), ('management', 'Management'), ('arts', 'Arts'), ('law', 'Law'), ('pharmacy', 'Pharmacy')], max_length=20)),
                ('established', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('description', models.TextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='colleges/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        
        # Create Blog model
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField(blank=True, max_length=300)),
                ('featured_image', models.ImageField(blank=True, upload_to='blogs/')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        
        # Remove old fields from Course
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='duration_months',
        ),
        migrations.RemoveField(
            model_name='course',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_active',
        ),
        
        # Add new fields to Course
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=20, unique=True, default='TEMP001'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('engineering', 'Engineering'), ('medical', 'Medical'), ('management', 'Management'), ('arts', 'Arts'), ('law', 'Law'), ('pharmacy', 'Pharmacy')], max_length=20, default='engineering'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=50, default='4 Years'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='degree_type',
            field=models.CharField(choices=[('undergraduate', 'Undergraduate'), ('postgraduate', 'Postgraduate'), ('diploma', 'Diploma')], max_length=20, default='undergraduate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='eligibility',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='annual_fee',
            field=models.DecimalField(decimal_places=2, max_digits=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='total_fee',
            field=models.DecimalField(decimal_places=2, max_digits=10, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.college'),
        ),
        
        # Create Review model
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='courses.college')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='students.student')),
            ],
        ),
    ]