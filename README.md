# E-Consultancy Backend

A Django REST API backend for the E-Consultancy educational platform.

## Features

- **User Management**: Authentication, roles, and user profiles
- **Student Management**: Student profiles and information
- **College Management**: College listings with details and ratings
- **Course Management**: Course catalog with categories and pricing
- **Application Management**: Student applications to courses
- **Payment Management**: Payment tracking and processing
- **Blog System**: Content management for educational blogs
- **Review System**: Student reviews and ratings
- **Admin Dashboard**: Statistics and management interface

## Technology Stack

- **Django 4.1.4**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (development)
- **Token Authentication**: API security
- **CORS Headers**: Cross-origin support
- **Pillow**: Image handling

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Sample Data
```bash
python manage.py create_sample_data
```

### 4. Start Server
```bash
python manage.py runserver
```



## API Endpoints

The API is available at `http://localhost:8000/api/`

### Authentication
- `POST /api/auth/login/` - Login
- `POST /api/auth/register/` - Register
- `POST /api/auth/logout/` - Logout

### Main Resources
- `/api/users/` - User management
- `/api/students/` - Student profiles
- `/api/colleges/` - College listings
- `/api/courses/` - Course catalog
- `/api/applications/` - Applications
- `/api/payments/` - Payments
- `/api/blogs/` - Blog posts
- `/api/reviews/` - Reviews and ratings

### Statistics
- `/api/dashboard/stats/` - Overall statistics
- `/api/students/stats/` - Student statistics
- `/api/colleges/stats/` - College statistics
- `/api/courses/stats/` - Course statistics
- `/api/applications/stats/` - Application statistics
- `/api/payments/stats/` - Payment statistics

## Default Credentials (Development Only)

**Admin User:**
- Username: `admin`
- Password: `admin123`

**Note:** Change default credentials in production!

## Admin Interface

Access the Django admin at: `http://localhost:8000/admin/`

## Database Models

### Core Models
- **User**: Extended Django user with roles
- **Role**: User role definitions
- **Student**: Student profile information
- **College**: Educational institutions
- **Course**: Academic programs
- **Application**: Student course applications
- **Payment**: Payment records
- **Blog**: Content management
- **Review**: Student feedback

## API Authentication

Use Token authentication by including the token in headers:
```
Authorization: Token your_token_here
```

Get token by logging in:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

## Development

### Project Structure
```
E-consultancyBackend/
├── eConsultancy/          # Main project settings
├── users/                 # User management app
├── students/              # Student management app
├── courses/               # Course and college management
├── applications/          # Application management
├── payments/              # Payment management
├── requirements.txt       # Dependencies
├── manage.py             # Django management
└── db.sqlite3            # Database file
```

### Adding New Features
1. Create new Django apps: `python manage.py startapp appname`
2. Add models in `models.py`
3. Create serializers in `serializers.py`
4. Add views in `views.py`
5. Configure URLs in `urls.py`
6. Run migrations: `python manage.py makemigrations && python manage.py migrate`

## Production Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed AWS deployment instructions.

### Quick Production Setup
1. Copy `.env.example` to `.env` and configure
2. Use `eConsultancy.settings_prod` for production
3. Set up PostgreSQL database on AWS RDS
4. Configure S3 for media files
5. Deploy using AWS Elastic Beanstalk or ECS

## Support

For issues and questions, refer to the API documentation in `API_DOCUMENTATION.md`.