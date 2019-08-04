from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Session


# from django.views.generic import *
# Create your views here.
def index(request):
    if auth.user_logged_in:
        return redirect('/home/')
    else:
        return redirect('/login/')

@login_required
def home_page(request):
    return render(request, 'auth/registered.html')


class SessionList(ListView):
    model = Session
    
class SessionDetail(DetailView):
    model = Session



@login_required
def submit_session(request):
    return render(request, 'app/submit_session.html')
