from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def challenges(request):
    return render(request, 'challenges.html')

def sample(request):
    return render(request, 'sample.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')