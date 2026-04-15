from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def home(request):
    return HttpResponse("Welcome to our Lawn Company website!")

def dashboard(request):
    return render(request, 'lawnApp/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'lawnApp/register.html', {'form': form})

def pricing(request):
    return render(request, 'lawnApp/price.html')

from django.shortcuts import render, redirect
from .models import Feedback

def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")

        if name and message:
            Feedback.objects.create(name=name, message=message)

        return redirect("feedback")

    reviews = Feedback.objects.all().order_by("-id")
    return render(request, "lawnApp/feedback.html", {"reviews": reviews})

