from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'solarpv/index.html')

def register(request):
    return render(request, 'solarpv/register.html')

def dashboard(request):
    return render(request, 'solarpv/dashboard.html')
