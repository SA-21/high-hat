from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Sample

def home(request):
    return render(request, 'home.html')

def challenges(request):
    return render(request, 'challenges.html')

def samples(request):
    samples = Sample.objects.all()
    return render(request, 'samples.html',{'samples': samples})

def sample(request, sample_id):
    sampledetails = get_object_or_404(Sample, pk = sample_id)
    return render(request, 'sample.html', {'sampledetails' : sampledetails})

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request,user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def dashboard(request):
    return render(request, 'dashboard.html')

