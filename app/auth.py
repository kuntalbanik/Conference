'''
Created on Aug 3, 2019

@author: kuntal
'''
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request, "auth/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # make sure the username & password is good
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:  # User was found & password matched
            if user.is_active:
                # associate the user with the sessioon
                auth.login(request, user)
                
                # read the destination
                next = ""
                if "next" in request.GET:
                    next = request.GET["next"]
                if next == None or next == "":
                    next = "/home_page/"
                return redirect(next)
            else:
                # account disabled
                return render(request, "auth/login.html", {"warning": "Your account is disabled"})
        else:
            # Bad username & password
            return render(request, "auth/login.html", {"warning": "Invalid username and or password"})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == "GET":
        return render(request, "auth/register.html")
    elif request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # call create_user from the ORM. Make sure you call save !
        auth.models.User.objects.create_user(username, email, password).save()
        # log the user in
        user = auth.authenticate(username=username, password=password)
        auth.login(request, user)
        return render(request, "auth/registered.html")
        

