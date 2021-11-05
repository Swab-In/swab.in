from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.models import UserProfile
from user.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from .forms import UserRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
import json

# def Userlogin(request):
#     form = UserLoginForm()
#     data = {
#         'form':form,
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         user = authenticate(request,username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return JsonResponse({"status":"User Login Success"})
#             # return redirect('Landing Page')
#         else:
#             return JsonResponse({"status":"Invalid Credential"})


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
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                response['status'] = "User Login Success"
                return JsonResponse(json.dumps(response), content_type="application/json", safe=False)
            else:
                response['status'] = "Invalid Credential"
                return JsonResponse(json.dumps(response), content_type="application/json", safe=False)

    return HttpResponse(response)
#

#         if user is not None:
#             login(request, user)
#             return JsonResponse({"status":"User Login Success"})
#             # return redirect('Landing Page')
#         else:
#             return JsonResponse({"status":"Invalid Credential"})

    # return render(request, template_name='login.html', context=data)


def UserRegister(request):
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
            return JsonResponse("user berhasil dibuat.", safe=False)

        if(password != re_password):
            messages.error(request, 'Password tidak cocok')

    return render(request, template_name='register.html')
