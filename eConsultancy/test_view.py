from django.http import HttpResponse

def test_swagger(request):
    return HttpResponse("Swagger test works!")