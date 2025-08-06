# E-Consultancy Backend API Documentation

## Base URL
```
http://localhost:8000/api/
```

## Authentication
The API uses Token-based authentication. Include the token in the Authorization header:
```
Authorization: Token your_token_here
```

## Endpoints

### Authentication
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration  
- `POST /api/auth/logout/` - User logout

### Users
- `GET /api/users/` - List all users
- `POST /api/users/` - Create new user
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user

### Roles
- `GET /api/roles/` - List all roles
- `POST /api/roles/` - Create new role

### Students
- `GET /api/students/` - List all students
- `POST /api/students/` - Create new student
- `GET /api/students/{id}/` - Get student details
- `PUT /api/students/{id}/` - Update student
- `DELETE /api/students/{id}/` - Delete student
- `GET /api/students/stats/` - Get student statistics

### Colleges
- `GET /api/colleges/` - List all colleges
- `POST /api/colleges/` - Create new college
- `GET /api/colleges/{id}/` - Get college details
- `PUT /api/colleges/{id}/` - Update college
- `DELETE /api/colleges/{id}/` - Delete college
- `GET /api/colleges/stats/` - Get college statistics

### Courses
- `GET /api/courses/` - List all courses
- `POST /api/courses/` - Create new course
- `GET /api/courses/{id}/` - Get course details
- `PUT /api/courses/{id}/` - Update course
- `DELETE /api/courses/{id}/` - Delete course
- `POST /api/courses/{id}/toggle-status/` - Toggle course status
- `GET /api/courses/stats/` - Get course statistics

### Applications
- `GET /api/applications/` - List all applications
- `POST /api/applications/` - Create new application
- `GET /api/applications/{id}/` - Get application details
- `PUT /api/applications/{id}/` - Update application
- `DELETE /api/applications/{id}/` - Delete application
- `GET /api/applications/stats/` - Get application statistics

### Payments
- `GET /api/payments/` - List all payments
- `POST /api/payments/` - Create new payment
- `GET /api/payments/{id}/` - Get payment details
- `PUT /api/payments/{id}/` - Update payment
- `DELETE /api/payments/{id}/` - Delete payment
- `GET /api/payments/stats/` - Get payment statistics

### Blogs
- `GET /api/blogs/` - List all blogs
- `POST /api/blogs/` - Create new blog
- `GET /api/blogs/{id}/` - Get blog details
- `PUT /api/blogs/{id}/` - Update blog
- `DELETE /api/blogs/{id}/` - Delete blog

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create new review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

### Dashboard
- `GET /api/dashboard/stats/` - Get overall dashboard statistics

## Sample Login Request
```json
POST /api/auth/login/
{
    "username": "admin",
    "password": "admin123"
}
```

## Sample Response
```json
{
    "token": "your_auth_token_here",
    "user": {
        "id": 1,
        "username": "admin",
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User"
    }
}
```

## Running the Server
```bash
cd E-consultancyBackend
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`