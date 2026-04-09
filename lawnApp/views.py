from django.shortcuts import render

def dashboard(request):
    return render(request, 'lawnApp/dashboard.html')

def login_view(request):
    return render(request, 'lawnApp/login.html')

def pricing(request):
    return render(request, 'lawnApp/price.html')