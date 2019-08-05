from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import *
from .models import Session
from django.core.urlresolvers import reverse_lazy
# To protect class based views use the following module
from django.contrib.auth.mixins import LoginRequiredMixin
# To use custom forms  from 'forms.py' file
from .forms import SessionForm  

# To protect class based views use the following module
# from django.utils.decorators import method_decorator
# Using the below decorator class views can be required login
# @method_decorator(login_required, name='dispatch')


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

# Creating class based views

class SessionList(ListView):
    model = Session
    
class SessionDetail(DetailView):
    model = Session

# Create Sessions
class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    # Using form fields from 'forms.py' file
    form_class = SessionForm
    # Manual from field setup here
    # fields = ['title', 'abstract', 'track', 'speaker']

# Update Session
class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    # Using form fields from 'forms.py' file
    form_class = SessionForm
    # Manual from field setup here
    # fields = ['title', 'abstract', 'track', 'speaker']

# Create Sessions
class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    # needs to match the name of the view I want to send the user back to
    success_url = reverse_lazy('sessions_list') 


# @login_required
# def submit_session(request):
#     return render(request, 'app/submit_session.html')
