from django.http import HttpResponse

def swagger_ui(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>E-Consultancy API Documentation</title>
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui.css" />
    </head>
    <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@3.25.0/swagger-ui-bundle.js"></script>
        <script>
            SwaggerUIBundle({
                url: '/api/schema/',
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
    schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "E-Consultancy API",
            "version": "1.0.0",
            "description": "Educational Consultancy Platform API"
        },
        "paths": {
            "/api/auth/login/": {
                "post": {
                    "summary": "User Login",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "username": {"type": "string"},
                                        "password": {"type": "string"}
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/api/users/": {
                "get": {"summary": "List Users"},
                "post": {"summary": "Create User"}
            },
            "/api/students/": {
                "get": {"summary": "List Students"},
                "post": {"summary": "Create Student"}
            },
            "/api/colleges/": {
                "get": {"summary": "List Colleges"},
                "post": {"summary": "Create College"}
            },
            "/api/courses/": {
                "get": {"summary": "List Courses"},
                "post": {"summary": "Create Course"}
            }
        }
    }
    
    import json
    return HttpResponse(json.dumps(schema), content_type='application/json')