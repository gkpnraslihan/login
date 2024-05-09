from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login():
    print("custom_login içerisinde")
    return redirect('login.html')

def custom_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')
