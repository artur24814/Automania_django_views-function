from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {'error': 'Invalid username or password'}
            return render(request, 'accounts/login.html', context)
        login(request, user)
        return redirect('/')
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        redirect('/login/')
    return render(request, 'accounts/logout.html', {})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/')
    return render(request, 'accounts/register.html',{})
