from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect

import json

def login_page(request):
    Username = request.POST.get('username')
    Password = request.POST.get('password')
    if Username is not None and Password is not None:
        ret = auth_and_login(request, Username, Password)
        if ret == 'Success':
            return HttpResponseRedirect('/accounts/profile/')
        elif ret == 'Disabled':
            return render(request, 'accounts/login.html', dict(csrf(request),
                                                            error="Account has been disabled"))
        elif ret == 'WrongPassword':
            Error = "Incorrect username and/or password"
            return render(request, 'accounts/login.html', dict(csrf(request),
                                                            error=Error))
        else:
            Error = "No account under that username found"
            return render(request, 'accounts/login.html', dict(csrf(request),
                                                            error=Error))
    else:
        return render(request, 'accounts/login.html', dict(csrf(request),
                                                            error=None))
                                                            
def profile(request):
    return render(request, 'accounts/profile.html')
    
def sign_up(request):
    Username = request.POST.get('username')
    First_name = request.POST.get('first_name')
    Last_name = request.POST.get('last_name')
    Email = request.POST.get('email')
    Password = request.POST.get('password')
    
    if Username is None or First_name is None or Last_name is None or Email is None or Password is None:
        return render(request, 'accounts/sign_up.html', dict(csrf(request),
                                                        error=None))
    else:
        Error = None
        try:
            u = User.objects.create_user(username=Username, first_name=First_name,
                                         last_name=Last_name, email=Email, password=Password)
        except:
            Error = "Sorry, error while creating user. Try again"
            return render(request, 'accounts/sign_up.html', dict(csrf(request),
                                                                        error=Error))
        return login_page(request)

def auth_and_login(request, Username, Password):
    user = authenticate(username=Username, password=Password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return 'Success'
        else:
            return 'Disabled'
    else:
        try:
            u = User.objects.get(username=Username)
            return 'WrongPassword'
        except:
            return 'NoUser'  
    
def check_username(request):
    if request.method == 'POST' and request.is_ajax():
        Username = request.POST.get("username")
        try:
            u = User.objects.get(username=Username)
            print("User exists")
            status = False
        except:
            status = True
            print("User DNE")
            
        return HttpResponse(json.dumps({'available': status}), content_type="application/json")
    else:
        return HttpResponse("Non post or non ajax request")