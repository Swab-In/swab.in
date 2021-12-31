from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
import json

def Userlogout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


def Userlogin(request):
    if request.user.is_authenticated:
        return redirect("/")

    return render(request, "login.html")


def authenticate_login(request):
    response = {}
    response['status'] = "Invalid Credential"
    form = AuthenticationForm(request, data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'User Login Success!')
                response['status'] = "User Login Success"
        else:
            response['status'] = "Invalid Credential"

    return JsonResponse(response)


def UserRegister(request):
    response = {}
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        password = request.POST.get('password1')
        re_password = request.POST.get('password2')

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Selamat user berhasil dibuat!')
            return redirect('/login/')

        if(password != re_password):
            response['message'] = 'Password tidak cocok.'

    return render(request, 'register.html', response)