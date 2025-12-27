from django.http import JsonResponse, HttpResponse

def swagger_ui(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>E-Consultancy API Documentation</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui.css" />
        <style>
            body { margin: 0; padding: 20px; }
            .swagger-ui .topbar { display: none; }
        </style>
    </head>
    <body>
        <h1>E-Consultancy Backend API - Complete Documentation</h1>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui-bundle.js"></script>
        <script>
            SwaggerUIBundle({
                url: '/api-schema/',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.presets.standalone
                ]
            });
        </script>
    </body>
    </html>
    """
    return HttpResponse(html)

def api_schema(request):
    protocol = 'https' if request.is_secure() else 'http'
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "E-Consultancy Backend API - Complete Documentation",
            "version": "1.0.0",
            "description": "Complete REST API for E-Consultancy educational platform with all CRUD operations, authentication, and statistics endpoints."
        },
        "servers": [
            {"url": f"{protocol}://{request.get_host()}"}
        ],
        "paths": {
            "/api/": {
                "get": {"tags": ["API Root"], "summary": "API Root", "description": "Get API information and available endpoints", "responses": {"200": {"description": "API information"}}}
            },

            "/api/users/": {
                "get": {"tags": ["Users"], "summary": "List Users", "description": "Get all users with pagination and search", "responses": {"200": {"description": "List of users"}}},
                "post": {
                    "tags": ["Users"], 
                    "summary": "Create User", 
                    "description": "Create a new user account",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {"type": "string"},
                                        "email": {"type": "string"},
                                        "password": {"type": "string"},
                                        "first_name": {"type": "string"},
                                        "last_name": {"type": "string"},
                                        "phone": {"type": "string"},
                                        "address": {"type": "string"},
                                        "role_id": {"type": "integer"}
                                    },
                                    "required": ["username", "email", "password"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "User created"}}
                }
            },
            "/api/users/admin/": {
                "post": {
                    "tags": ["Users"], 
                    "summary": "Create Admin User", 
                    "description": "Create a new admin user account (staff access)",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {"type": "string"},
                                        "email": {"type": "string"},
                                        "password": {"type": "string"},
                                        "first_name": {"type": "string"},
                                        "last_name": {"type": "string"},
                                        "phone": {"type": "string"},
                                        "address": {"type": "string"}
                                    },
                                    "required": ["username", "email", "password"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Admin user created"}}
                }
            },
            "/api/users/{id}/": {
                "get": {"tags": ["Users"], "summary": "Get User", "description": "Get specific user details", "responses": {"200": {"description": "User details"}}},
                "put": {"tags": ["Users"], "summary": "Update User", "description": "Update user information", "responses": {"200": {"description": "User updated"}}},
                "delete": {"tags": ["Users"], "summary": "Delete User", "description": "Delete user account", "responses": {"204": {"description": "User deleted"}}}
            },
            "/api/roles/": {
                "get": {"tags": ["Users"], "summary": "List Roles", "description": "Get all user roles", "responses": {"200": {"description": "List of roles"}}},
                "post": {"tags": ["Users"], "summary": "Create Role", "description": "Create a new user role", "responses": {"201": {"description": "Role created"}}}
            },
            "/api/auth/login/": {
                "post": {
                    "tags": ["Authentication"], 
                    "summary": "User Login", 
                    "description": "Authenticate user and get token",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {"type": "string"},
                                        "password": {"type": "string"}
                                    },
                                    "required": ["username", "password"]
                                }
                            }
                        }
                    },
                    "responses": {"200": {"description": "Login successful with token"}}
                }
            },
            "/api/auth/register/": {
                "post": {
                    "tags": ["Authentication"], 
                    "summary": "User Registration", 
                    "description": "Register new user account",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {"type": "string"},
                                        "email": {"type": "string"},
                                        "password": {"type": "string"},
                                        "first_name": {"type": "string"},
                                        "last_name": {"type": "string"},
                                        "phone": {"type": "string"},
                                        "address": {"type": "string"},
                                        "role_id": {"type": "integer"}
                                    },
                                    "required": ["username", "email", "password"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "User registered with token"}}
                }
            },
            "/api/auth/logout/": {
                "post": {"tags": ["Authentication"], "summary": "User Logout", "description": "Logout and invalidate token", "responses": {"200": {"description": "Logout successful"}}}
            },
            "/api/students/": {
                "get": {"tags": ["Students"], "summary": "List Students", "description": "Get all student profiles with search", "responses": {"200": {"description": "List of students"}}},
                "post": {
                    "tags": ["Students"], 
                    "summary": "Create Student", 
                    "description": "Create new student profile",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "user_id": {"type": "integer"},
                                        "date_of_birth": {"type": "string", "format": "date"},
                                        "nationality": {"type": "string"},
                                        "guardian_name": {"type": "string"},
                                        "guardian_contact": {"type": "string"}
                                    },
                                    "required": ["user_id"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Student created"}}
                }
            },
            "/api/students/{id}/": {
                "get": {"tags": ["Students"], "summary": "Get Student", "description": "Get specific student details", "responses": {"200": {"description": "Student details"}}},
                "put": {"tags": ["Students"], "summary": "Update Student", "description": "Update student information", "responses": {"200": {"description": "Student updated"}}},
                "delete": {"tags": ["Students"], "summary": "Delete Student", "description": "Delete student profile", "responses": {"204": {"description": "Student deleted"}}}
            },
            "/api/students/stats/": {
                "get": {"tags": ["Students"], "summary": "Student Statistics", "description": "Get student statistics (total, active, inactive)", "responses": {"200": {"description": "Student statistics"}}}
            },
            "/api/colleges/": {
                "get": {"tags": ["Colleges"], "summary": "List Colleges", "description": "Get all colleges with search by name/location", "responses": {"200": {"description": "List of colleges"}}},
                "post": {
                    "tags": ["Colleges"], 
                    "summary": "Create College", 
                    "description": "Create new college",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "short_name": {"type": "string"},
                                        "location": {"type": "string"},
                                        "type": {"type": "string"},
                                        "established": {"type": "string"},
                                        "ranking": {"type": "integer"},
                                        "rating": {"type": "number"},
                                        "website": {"type": "string"},
                                        "email": {"type": "string"},
                                        "phone": {"type": "string"},
                                        "description": {"type": "string"},
                                        "image": {"type": "string"}
                                    },
                                    "required": ["name"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "College created"}}
                }
            },
            "/api/colleges/{id}/": {
                "get": {"tags": ["Colleges"], "summary": "Get College", "description": "Get specific college details", "responses": {"200": {"description": "College details"}}},
                "put": {"tags": ["Colleges"], "summary": "Update College", "description": "Update college information", "responses": {"200": {"description": "College updated"}}},
                "delete": {"tags": ["Colleges"], "summary": "Delete College", "description": "Delete college", "responses": {"204": {"description": "College deleted"}}}
            },
            "/api/colleges/stats/": {
                "get": {"tags": ["Colleges"], "summary": "College Statistics", "description": "Get college statistics by type and status", "responses": {"200": {"description": "College statistics"}}}
            },
            "/api/courses/": {
                "get": {"tags": ["Courses"], "summary": "List Courses", "description": "Get all courses with search by name/code", "responses": {"200": {"description": "List of courses"}}},
                "post": {
                    "tags": ["Courses"], 
                    "summary": "Create Course", 
                    "description": "Create new course",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "code": {"type": "string"},
                                        "category": {"type": "string"},
                                        "duration": {"type": "string"},
                                        "degree_type": {"type": "string"},
                                        "description": {"type": "string"},
                                        "eligibility": {"type": "string"},
                                        "fee": {"type": "string"},
                                        "college_id": {"type": "integer"},
                                        "image": {"type": "string"}
                                    },
                                    "required": ["name", "code", "college_id"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Course created"}}
                }
            },
            "/api/courses/{id}/": {
                "get": {"tags": ["Courses"], "summary": "Get Course", "description": "Get specific course details", "responses": {"200": {"description": "Course details"}}},
                "put": {"tags": ["Courses"], "summary": "Update Course", "description": "Update course information", "responses": {"200": {"description": "Course updated"}}},
                "delete": {"tags": ["Courses"], "summary": "Delete Course", "description": "Delete course", "responses": {"204": {"description": "Course deleted"}}}
            },
            "/api/courses/{id}/toggle-status/": {
                "post": {"tags": ["Courses"], "summary": "Toggle Course Status", "description": "Toggle course between active/inactive", "responses": {"200": {"description": "Course status toggled"}}}
            },
            "/api/courses/stats/": {
                "get": {"tags": ["Courses"], "summary": "Course Statistics", "description": "Get course statistics by category and status", "responses": {"200": {"description": "Course statistics"}}}
            },
            "/api/blogs/": {
                "get": {"tags": ["Content Management"], "summary": "List Blogs", "description": "Get all blog posts with search", "responses": {"200": {"description": "List of blogs"}}},
                "post": {
                    "tags": ["Content Management"], 
                    "summary": "Create Blog", 
                    "description": "Create new blog post",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "title": {"type": "string"},
                                        "slug": {"type": "string"},
                                        "content": {"type": "string"},
                                        "excerpt": {"type": "string"},
                                        "featured_image": {"type": "string"},
                                        "status": {"type": "string"},
                                        "author_id": {"type": "integer"}
                                    },
                                    "required": ["title", "content"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Blog created"}}
                }
            },
            "/api/blogs/{id}/": {
                "get": {"tags": ["Content Management"], "summary": "Get Blog", "description": "Get specific blog post", "responses": {"200": {"description": "Blog details"}}},
                "put": {"tags": ["Content Management"], "summary": "Update Blog", "description": "Update blog post", "responses": {"200": {"description": "Blog updated"}}},
                "delete": {"tags": ["Content Management"], "summary": "Delete Blog", "description": "Delete blog post", "responses": {"204": {"description": "Blog deleted"}}}
            },
            "/api/reviews/": {
                "get": {"tags": ["Content Management"], "summary": "List Reviews", "description": "Get all reviews with search", "responses": {"200": {"description": "List of reviews"}}},
                "post": {
                    "tags": ["Content Management"], 
                    "summary": "Create Review", 
                    "description": "Create new review",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "student_id": {"type": "integer"},
                                        "college_id": {"type": "integer"},
                                        "course_id": {"type": "integer"},
                                        "rating": {"type": "number"},
                                        "title": {"type": "string"},
                                        "content": {"type": "string"}
                                    },
                                    "required": ["rating", "content"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Review created"}}
                }
            },
            "/api/reviews/{id}/": {
                "get": {"tags": ["Content Management"], "summary": "Get Review", "description": "Get specific review", "responses": {"200": {"description": "Review details"}}},
                "put": {"tags": ["Content Management"], "summary": "Update Review", "description": "Update review", "responses": {"200": {"description": "Review updated"}}},
                "delete": {"tags": ["Content Management"], "summary": "Delete Review", "description": "Delete review", "responses": {"204": {"description": "Review deleted"}}}
            },
            "/api/applications/": {
                "get": {"tags": ["Applications"], "summary": "List Applications", "description": "Get all student applications with search", "responses": {"200": {"description": "List of applications"}}},
                "post": {
                    "tags": ["Applications"], 
                    "summary": "Create Application", 
                    "description": "Submit new application",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "student_id": {"type": "integer"},
                                        "course_id": {"type": "integer"},
                                        "status": {"type": "string"},
                                        "remarks": {"type": "string"}
                                    },
                                    "required": ["student_id", "course_id"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Application created"}}
                }
            },
            "/api/applications/{id}/": {
                "get": {"tags": ["Applications"], "summary": "Get Application", "description": "Get specific application details", "responses": {"200": {"description": "Application details"}}},
                "put": {"tags": ["Applications"], "summary": "Update Application", "description": "Update application status/details", "responses": {"200": {"description": "Application updated"}}},
                "delete": {"tags": ["Applications"], "summary": "Delete Application", "description": "Delete application", "responses": {"204": {"description": "Application deleted"}}}
            },
            "/api/applications/stats/": {
                "get": {"tags": ["Applications"], "summary": "Application Statistics", "description": "Get application statistics by status", "responses": {"200": {"description": "Application statistics"}}}
            },
            "/api/payments/": {
                "get": {"tags": ["Payments"], "summary": "List Payments", "description": "Get all payment records", "responses": {"200": {"description": "List of payments"}}},
                "post": {
                    "tags": ["Payments"], 
                    "summary": "Create Payment", 
                    "description": "Process new payment",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "application_id": {"type": "integer"},
                                        "amount": {"type": "string"},
                                        "payment_method": {"type": "string"},
                                        "transaction_id": {"type": "string"},
                                        "status": {"type": "string"}
                                    },
                                    "required": ["application_id", "amount"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Payment created"}}
                }
            },
            "/api/payments/{id}/": {
                "get": {"tags": ["Payments"], "summary": "Get Payment", "description": "Get specific payment details", "responses": {"200": {"description": "Payment details"}}},
                "put": {"tags": ["Payments"], "summary": "Update Payment", "description": "Update payment information", "responses": {"200": {"description": "Payment updated"}}},
                "delete": {"tags": ["Payments"], "summary": "Delete Payment", "description": "Delete payment record", "responses": {"204": {"description": "Payment deleted"}}}
            },
            "/api/payments/stats/": {
                "get": {"tags": ["Payments"], "summary": "Payment Statistics", "description": "Get payment statistics", "responses": {"200": {"description": "Payment statistics"}}}
            },
            "/api/advertisements/": {
                "get": {"tags": ["Advertisements"], "summary": "List Advertisements", "description": "Get all advertisements", "responses": {"200": {"description": "List of advertisements"}}},
                "post": {
                    "tags": ["Advertisements"], 
                    "summary": "Create Advertisement", 
                    "description": "Create new advertisement",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "title": {"type": "string"},
                                        "subtitle": {"type": "string"},
                                        "description": {"type": "string"},
                                        "button_text": {"type": "string"},
                                        "image": {"type": "string"},
                                        "is_active": {"type": "boolean"},
                                        "order": {"type": "integer"}
                                    },
                                    "required": ["title"]
                                }
                            }
                        }
                    },
                    "responses": {"201": {"description": "Advertisement created"}}
                }
            },
            "/api/advertisements/{id}/": {
                "get": {"tags": ["Advertisements"], "summary": "Get Advertisement", "description": "Get specific advertisement", "responses": {"200": {"description": "Advertisement details"}}},
                "put": {"tags": ["Advertisements"], "summary": "Update Advertisement", "description": "Update advertisement", "responses": {"200": {"description": "Advertisement updated"}}},
                "patch": {"tags": ["Advertisements"], "summary": "Partial Update Advertisement", "description": "Partially update advertisement", "responses": {"200": {"description": "Advertisement updated"}}},
                "delete": {"tags": ["Advertisements"], "summary": "Delete Advertisement", "description": "Delete advertisement", "responses": {"204": {"description": "Advertisement deleted"}}}
            }
        }
    }
    return JsonResponse(schema)