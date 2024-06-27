# app_name/views.py
from django.http import HttpResponse
import os

def serve_index(request, *args, **kwargs):
    frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'index.html')
    with open(frontend_path, 'r') as f:
        return HttpResponse(f.read(), content_type='text/html')
