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
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def Userlogout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")


@csrf_exempt
def Userlogin(request):
    if request.user.is_authenticated:
        return redirect("/")

    return render(request, "login.html")


@csrf_exempt
def authenticate_login(request):
    data = {"status": "Login gagal.", "success": False}
    if request.method == "POST":
        print(request.body)

        user_data = json.loads(request.body)
        username = user_data['username']
        password = user_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            data['user_id'] = user.pk
            data['status'] = "Login berhasil."
            data['success'] = True

    return JsonResponse(data)


@csrf_exempt
def UserRegister(request):
    data = {"status": "Registrasi gagal.", "success": False}
    # response = {}
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        register_data = json.loads(request.body)
        form = UserRegistrationForm(register_data)
        # form = UserRegistrationForm(request.POST)
        # password = request.POST.get('password1')
        # re_password = request.POST.get('password2')
        if form.is_valid():
            # user = form.save()
            form.save()
            # login(request, user)
            # messages.success(request, 'Selamat user berhasil dibuat!')
            # return redirect('/login/')
            data['status'] = "Registrasi berhasil."
            data['success'] = True

    return JsonResponse(data)

    #     if(password != re_password):
    #         response['message'] = 'Password tidak cocok.'

    # return render(request, 'register.html', response)
