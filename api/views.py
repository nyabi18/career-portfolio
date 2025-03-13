from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "API is working!"})

# Create your views here.
