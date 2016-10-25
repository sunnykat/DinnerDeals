from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


# Create your views here.
def splash (request):
    context={
    }
    return render(request, 'login/base.html', context)
def login_page (request):
    return render(request, 'login/login.html')

def login (request):
    pass
def register(request):
    return render (request, 'login/register.html')
def create_user(request):

    errors= User.objects.reg_validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('login:register')
    return redirect('login:splash')
