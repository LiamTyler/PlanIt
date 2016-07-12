from django.shortcuts import render
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect

def login_page(request):
    return render(request, 'accounts/login.html', dict(csrf(request),
                                                       failed_to_auth=False,))
def profile(request):
    print("in profile")
    return render(request, 'accounts/profile.html')
    
def sign_up(request):
    return render(request, 'accounts/sign_up.html', dict(csrf(request),
                                                        user_already_exists=False,
                                                        passwords_didnt_match=False,
                                                        error_creating_user=False,
                                                        ))

def create_user(request):
    Username = request.POST.get('username')
    First_name = request.POST.get('first_name')
    Last_name = request.POST.get('last_name')
    Email = request.POST.get('email')
    Password = request.POST.get('password')
    password_retype = request.POST.get('password_retype')
    print("past posts")
    user_already_exists = False
    try:
        u = User.objects.get(username=Username)
        user_already_exists = True
    except:
        pass
    print("past test username")    
    passwords_didnt_match = False
    if Password != password_retype:
        passwords_didnt_match = True
        
    if user_already_exists or passwords_didnt_match:
        print("redo form")
        return render(request, 'accounts/sign_up.html', dict(csrf(request),
                                                        user_already_exists=user_already_exists,
                                                        passwords_didnt_match=passwords_didnt_match,
                                                        error_creating_user=False,
                                                        ))
    else:
        try:
            u = User.objects.create_user(username=Username, first_name=First_name,
                                         last_name=Last_name, email=Email, password=Password)
        except:
            print("redo for error while creating user")
            return render(request, 'accounts/sign_up.html', dict(csrf(request),
                                                        user_already_exists=False,
                                                        passwords_didnt_match=False,
                                                        error_creating_user=True,
                                                        ))
        
        print("auth user")
        auth_user(request)
        
def auth_user(request):
    print(request.user)
    username = request.POST.get('username')
    password = request.POST.get('password')
    print("username: ", username, "\nPassword: ", password)
    user = authenticate(username=username, password=password)
    if user is not None:
        print("User was not none")
        if user.is_active:
            print("attempting to login")
            login(request, user)
            print("login successful")
            return redirect('/accounts/profile/')
        else:
            # Return a 'disabled account' error message
            print("User exists, but account has been disabled.")
            return render(request, 'accounts/login.html', dict(csrf(request),
                                                       failed_to_auth=True,))
    else:
        # Return an 'invalid login' error message.
        print("Username and/or password were incorrect.")
        return render(request, 'accounts/login.html', dict(csrf(request),
                                                       failed_to_auth=True,))
                                                       
    print("Idk how the fuck we got here")
    
    
def logout(request):
    pass