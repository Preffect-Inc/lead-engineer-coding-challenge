from django.http import JsonResponse
from .models import User

def list_users(request):
    users_data = list(User.objects.values())
    return JsonResponse(users_data, safe=False)
