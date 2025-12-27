from django.http import HttpResponse
import json

def complete_swagger_ui(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>E-Consultancy API Documentation</title>
        <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui.css" />
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui-bundle.js"></script>
        <script>
            SwaggerUIBundle({
                url: '/complete-api-schema/',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.presets.standalone
                ]
            });
        </script>
    </body>
    </html>
    '''
    return HttpResponse(html)

def complete_api_schema(request):
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "E-Consultancy Platform API",
            "version": "1.0.0",
            "description": "Complete API documentation for Educational Consultancy Management System",
            "contact": {
                "name": "API Support",
                "email": "support@econsultancy.com"
            }
        },
        "servers": [
            {"url": ".", "description": "Development server"}
        ],
        "components": {
            "securitySchemes": {
                "TokenAuth": {
                    "type": "apiKey",
                    "in": "header",
                    "name": "Authorization",
                    "description": "Token-based authentication"
                }
            },
            "schemas": {
                "User": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "username": {"type": "string"},
                        "email": {"type": "string"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                        "phone": {"type": "string"},
                        "role": {"type": "string", "enum": ["admin", "student", "counselor"]},
                        "is_active": {"type": "boolean"},
                        "date_joined": {"type": "string", "format": "date-time"}
                    }
                },
                "Student": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "user": {"$ref": "#/components/schemas/User"},
                        "date_of_birth": {"type": "string", "format": "date"},
                        "gender": {"type": "string", "enum": ["M", "F", "O"]},
                        "address": {"type": "string"},
                        "city": {"type": "string"},
                        "state": {"type": "string"},
                        "pincode": {"type": "string"},
                        "qualification": {"type": "string"},
                        "percentage": {"type": "number"},
                        "preferred_course": {"type": "string"},
                        "budget": {"type": "number"},
                        "profile_picture": {"type": "string"}
                    }
                },
                "College": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "location": {"type": "string"},
                        "type": {"type": "string"},
                        "established": {"type": "integer"},
                        "rating": {"type": "number"},
                        "description": {"type": "string"},
                        "website": {"type": "string"},
                        "email": {"type": "string"},
                        "phone": {"type": "string"},
                        "status": {"type": "string", "enum": ["active", "inactive"]},
                        "image": {"type": "string"}
                    }
                },
                "Course": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "name": {"type": "string"},
                        "code": {"type": "string"},
                        "category": {"type": "string"},
                        "duration": {"type": "string"},
                        "degree_type": {"type": "string"},
                        "description": {"type": "string"},
                        "eligibility": {"type": "string"},
                        "annual_fee": {"type": "number"},
                        "total_fee": {"type": "number"},
                        "college": {"$ref": "#/components/schemas/College"},
                        "status": {"type": "string", "enum": ["active", "inactive"]}
                    }
                },
                "Application": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "student": {"$ref": "#/components/schemas/Student"},
                        "college": {"$ref": "#/components/schemas/College"},
                        "course": {"$ref": "#/components/schemas/Course"},
                        "status": {"type": "string", "enum": ["pending", "approved", "rejected", "completed"]},
                        "application_date": {"type": "string", "format": "date-time"},
                        "documents": {"type": "array", "items": {"type": "string"}},
                        "remarks": {"type": "string"}
                    }
                },
                "Payment": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "application": {"$ref": "#/components/schemas/Application"},
                        "amount": {"type": "number"},
                        "payment_method": {"type": "string"},
                        "transaction_id": {"type": "string"},
                        "status": {"type": "string", "enum": ["pending", "completed", "failed", "refunded"]},
                        "payment_date": {"type": "string", "format": "date-time"}
                    }
                },
                "Blog": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "title": {"type": "string"},
                        "slug": {"type": "string"},
                        "content": {"type": "string"},
                        "excerpt": {"type": "string"},
                        "author": {"$ref": "#/components/schemas/User"},
                        "category": {"type": "string"},
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "featured_image": {"type": "string"},
                        "status": {"type": "string", "enum": ["draft", "published", "archived"]},
                        "published_at": {"type": "string", "format": "date-time"},
                        "views": {"type": "integer"},
                        "likes": {"type": "integer"}
                    }
                }
            }
        },
        "paths": {
            "/api/auth/login/": {
                "post": {
                    "tags": ["Authentication"],
                    "summary": "User Login",
                    "description": "Authenticate user and get access token",
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
                    "responses": {
                        "200": {
                            "description": "Login successful",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "token": {"type": "string"},
                                            "user": {"$ref": "#/components/schemas/User"}
                                        }
                                    }
                                }
                            }
                        },
                        "401": {"description": "Invalid credentials"}
                    }
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
                                        "role": {"type": "string", "enum": ["student", "counselor"]}
                                    },
                                    "required": ["username", "email", "password"]
                                }
                            }
                        }
                    },
                    "responses": {
                        "201": {"description": "User created successfully"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/auth/logout/": {
                "post": {
                    "tags": ["Authentication"],
                    "summary": "User Logout",
                    "security": [{"TokenAuth": []}],
                    "responses": {
                        "200": {"description": "Logout successful"}
                    }
                }
            },
            "/api/users/": {
                "get": {
                    "tags": ["Users"],
                    "summary": "List Users",
                    "security": [{"TokenAuth": []}],
                    "parameters": [
                        {"name": "role", "in": "query", "schema": {"type": "string"}},
                        {"name": "is_active", "in": "query", "schema": {"type": "boolean"}},
                        {"name": "search", "in": "query", "schema": {"type": "string"}}
                    ],
                    "responses": {
                        "200": {
                            "description": "List of users",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {"$ref": "#/components/schemas/User"}
                                    }
                                }
                            }
                        }
                    }
                },
                "post": {
                    "tags": ["Users"],
                    "summary": "Create User",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/User"}
                            }
                        }
                    },
                    "responses": {
                        "201": {"description": "User created"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/users/{id}/": {
                "get": {
                    "tags": ["Users"],
                    "summary": "Get User Details",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "200": {"description": "User details", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/User"}}}},
                        "404": {"description": "User not found"}
                    }
                },
                "put": {
                    "tags": ["Users"],
                    "summary": "Update User",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/User"}}}},
                    "responses": {
                        "200": {"description": "User updated"},
                        "404": {"description": "User not found"}
                    }
                },
                "delete": {
                    "tags": ["Users"],
                    "summary": "Delete User",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "204": {"description": "User deleted"},
                        "404": {"description": "User not found"}
                    }
                }
            },
            "/api/students/": {
                "get": {
                    "tags": ["Students"],
                    "summary": "List Students",
                    "security": [{"TokenAuth": []}],
                    "parameters": [
                        {"name": "city", "in": "query", "schema": {"type": "string"}},
                        {"name": "qualification", "in": "query", "schema": {"type": "string"}},
                        {"name": "preferred_course", "in": "query", "schema": {"type": "string"}}
                    ],
                    "responses": {
                        "200": {"description": "List of students", "content": {"application/json": {"schema": {"type": "array", "items": {"$ref": "#/components/schemas/Student"}}}}}
                    }
                },
                "post": {
                    "tags": ["Students"],
                    "summary": "Create Student Profile",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Student"}}}},
                    "responses": {
                        "201": {"description": "Student profile created"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/students/{id}/": {
                "get": {
                    "tags": ["Students"],
                    "summary": "Get Student Details",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "200": {"description": "Student details", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Student"}}}},
                        "404": {"description": "Student not found"}
                    }
                },
                "put": {
                    "tags": ["Students"],
                    "summary": "Update Student Profile",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Student"}}}},
                    "responses": {
                        "200": {"description": "Student updated"},
                        "404": {"description": "Student not found"}
                    }
                }
            },
            "/api/colleges/": {
                "get": {
                    "tags": ["Colleges"],
                    "summary": "List Colleges",
                    "parameters": [
                        {"name": "type", "in": "query", "schema": {"type": "string"}},
                        {"name": "location", "in": "query", "schema": {"type": "string"}},
                        {"name": "status", "in": "query", "schema": {"type": "string"}},
                        {"name": "search", "in": "query", "schema": {"type": "string"}}
                    ],
                    "responses": {
                        "200": {"description": "List of colleges", "content": {"application/json": {"schema": {"type": "array", "items": {"$ref": "#/components/schemas/College"}}}}}
                    }
                },
                "post": {
                    "tags": ["Colleges"],
                    "summary": "Create College",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/College"}}}},
                    "responses": {
                        "201": {"description": "College created"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/colleges/{id}/": {
                "get": {
                    "tags": ["Colleges"],
                    "summary": "Get College Details",
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "200": {"description": "College details", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/College"}}}},
                        "404": {"description": "College not found"}
                    }
                },
                "put": {
                    "tags": ["Colleges"],
                    "summary": "Update College",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/College"}}}},
                    "responses": {
                        "200": {"description": "College updated"},
                        "404": {"description": "College not found"}
                    }
                },
                "delete": {
                    "tags": ["Colleges"],
                    "summary": "Delete College",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "204": {"description": "College deleted"},
                        "404": {"description": "College not found"}
                    }
                }
            },
            "/api/courses/": {
                "get": {
                    "tags": ["Courses"],
                    "summary": "List Courses",
                    "parameters": [
                        {"name": "category", "in": "query", "schema": {"type": "string"}},
                        {"name": "degree_type", "in": "query", "schema": {"type": "string"}},
                        {"name": "college", "in": "query", "schema": {"type": "integer"}},
                        {"name": "min_fee", "in": "query", "schema": {"type": "number"}},
                        {"name": "max_fee", "in": "query", "schema": {"type": "number"}}
                    ],
                    "responses": {
                        "200": {"description": "List of courses", "content": {"application/json": {"schema": {"type": "array", "items": {"$ref": "#/components/schemas/Course"}}}}}
                    }
                },
                "post": {
                    "tags": ["Courses"],
                    "summary": "Create Course",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Course"}}}},
                    "responses": {
                        "201": {"description": "Course created"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/courses/{id}/": {
                "get": {
                    "tags": ["Courses"],
                    "summary": "Get Course Details",
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "200": {"description": "Course details", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Course"}}}},
                        "404": {"description": "Course not found"}
                    }
                },
                "put": {
                    "tags": ["Courses"],
                    "summary": "Update Course",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Course"}}}},
                    "responses": {
                        "200": {"description": "Course updated"},
                        "404": {"description": "Course not found"}
                    }
                },
                "delete": {
                    "tags": ["Courses"],
                    "summary": "Delete Course",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "204": {"description": "Course deleted"},
                        "404": {"description": "Course not found"}
                    }
                }
            },
            "/api/applications/": {
                "get": {
                    "tags": ["Applications"],
                    "summary": "List Applications",
                    "security": [{"TokenAuth": []}],
                    "parameters": [
                        {"name": "student", "in": "query", "schema": {"type": "integer"}},
                        {"name": "college", "in": "query", "schema": {"type": "integer"}},
                        {"name": "status", "in": "query", "schema": {"type": "string"}}
                    ],
                    "responses": {
                        "200": {"description": "List of applications", "content": {"application/json": {"schema": {"type": "array", "items": {"$ref": "#/components/schemas/Application"}}}}}
                    }
                },
                "post": {
                    "tags": ["Applications"],
                    "summary": "Submit Application",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Application"}}}},
                    "responses": {
                        "201": {"description": "Application submitted"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/applications/{id}/": {
                "get": {
                    "tags": ["Applications"],
                    "summary": "Get Application Details",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "200": {"description": "Application details", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Application"}}}},
                        "404": {"description": "Application not found"}
                    }
                },
                "put": {
                    "tags": ["Applications"],
                    "summary": "Update Application Status",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Application"}}}},
                    "responses": {
                        "200": {"description": "Application updated"},
                        "404": {"description": "Application not found"}
                    }
                }
            },
            "/api/payments/": {
                "get": {
                    "tags": ["Payments"],
                    "summary": "List Payments",
                    "security": [{"TokenAuth": []}],
                    "parameters": [
                        {"name": "application", "in": "query", "schema": {"type": "integer"}},
                        {"name": "status", "in": "query", "schema": {"type": "string"}}
                    ],
                    "responses": {
                        "200": {"description": "List of payments", "content": {"application/json": {"schema": {"type": "array", "items": {"$ref": "#/components/schemas/Payment"}}}}}
                    }
                },
                "post": {
                    "tags": ["Payments"],
                    "summary": "Process Payment",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Payment"}}}},
                    "responses": {
                        "201": {"description": "Payment processed"},
                        "400": {"description": "Payment failed"}
                    }
                }
            },
            "/api/blogs/": {
                "get": {
                    "tags": ["Blogs"],
                    "summary": "List Blog Posts",
                    "parameters": [
                        {"name": "category", "in": "query", "schema": {"type": "string"}},
                        {"name": "status", "in": "query", "schema": {"type": "string"}},
                        {"name": "author", "in": "query", "schema": {"type": "integer"}}
                    ],
                    "responses": {
                        "200": {"description": "List of blog posts", "content": {"application/json": {"schema": {"type": "array", "items": {"$ref": "#/components/schemas/Blog"}}}}}
                    }
                },
                "post": {
                    "tags": ["Blogs"],
                    "summary": "Create Blog Post",
                    "security": [{"TokenAuth": []}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Blog"}}}},
                    "responses": {
                        "201": {"description": "Blog post created"},
                        "400": {"description": "Validation error"}
                    }
                }
            },
            "/api/blogs/{id}/": {
                "get": {
                    "tags": ["Blogs"],
                    "summary": "Get Blog Post",
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "200": {"description": "Blog post details", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Blog"}}}},
                        "404": {"description": "Blog post not found"}
                    }
                },
                "put": {
                    "tags": ["Blogs"],
                    "summary": "Update Blog Post",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/Blog"}}}},
                    "responses": {
                        "200": {"description": "Blog post updated"},
                        "404": {"description": "Blog post not found"}
                    }
                },
                "delete": {
                    "tags": ["Blogs"],
                    "summary": "Delete Blog Post",
                    "security": [{"TokenAuth": []}],
                    "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "integer"}}],
                    "responses": {
                        "204": {"description": "Blog post deleted"},
                        "404": {"description": "Blog post not found"}
                    }
                }
            },
            "/api/dashboard/stats/": {
                "get": {
                    "tags": ["Dashboard"],
                    "summary": "Get Dashboard Statistics",
                    "security": [{"TokenAuth": []}],
                    "responses": {
                        "200": {
                            "description": "Dashboard statistics",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "total_students": {"type": "integer"},
                                            "total_colleges": {"type": "integer"},
                                            "total_courses": {"type": "integer"},
                                            "total_applications": {"type": "integer"},
                                            "pending_applications": {"type": "integer"},
                                            "approved_applications": {"type": "integer"},
                                            "total_payments": {"type": "number"},
                                            "monthly_growth": {
                                                "type": "object",
                                                "properties": {
                                                    "students": {"type": "integer"},
                                                    "applications": {"type": "integer"},
                                                    "payments": {"type": "number"}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/api/search/": {
                "get": {
                    "tags": ["Search"],
                    "summary": "Global Search",
                    "parameters": [
                        {"name": "q", "in": "query", "required": True, "schema": {"type": "string"}},
                        {"name": "type", "in": "query", "schema": {"type": "string", "enum": ["colleges", "courses", "blogs"]}}
                    ],
                    "responses": {
                        "200": {
                            "description": "Search results",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "colleges": {"type": "array", "items": {"$ref": "#/components/schemas/College"}},
                                            "courses": {"type": "array", "items": {"$ref": "#/components/schemas/Course"}},
                                            "blogs": {"type": "array", "items": {"$ref": "#/components/schemas/Blog"}}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    return HttpResponse(json.dumps(schema, indent=2), content_type='application/json')