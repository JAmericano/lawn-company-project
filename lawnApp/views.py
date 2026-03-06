from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to our Lawn Company website!")
# Create your views here.
