from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def index(request):
    return render(request, 'index.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
            else:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login_page')
        else:
            messages.error(request, 'Passwords do not match.')

    return render(request, 'register.html')





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful. Welcome!')
            return redirect('index')  # Redirect to 'index' or another valid page
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')






def logout_view(request):
    logout(request)
    return redirect('/')
