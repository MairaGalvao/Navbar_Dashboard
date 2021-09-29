from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def display_dashboard(request):
    return render(request, 'dashboard_template.html')