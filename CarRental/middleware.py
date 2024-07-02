
import os
from django.http import JsonResponse

class AdminAPIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.api_key = 'shrutikedari'

    def __call__(self, request):
        if request.path.startswith('/api/car/') and 'API-Key' not in request.headers:
            return JsonResponse({'error': 'Forbidden: API key required'}, status=403)

        api_key = request.headers.get('API-Key')
        if request.path.startswith('/api/car/') and api_key != self.api_key:
            return JsonResponse({'error': 'Forbidden: Invalid API key'}, status=403)
        if request.path.startswith('/api/car/details/postsave/') and api_key != self.api_key:
            return JsonResponse({'error': 'Forbidden: Invalid API key'}, status=403)

        response = self.get_response(request)
        return response