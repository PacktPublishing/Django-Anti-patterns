# views.py

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None

    return render(request, 'login.html', {'error_message': error_message})