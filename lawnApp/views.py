from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to our Lawn Company website!")

def dashboard(request):
    return render(request, 'lawnApp/dashboard.html')
