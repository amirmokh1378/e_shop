from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
import requests


# Create your views here.


# def login_page(request):
#     print(request.user)
#     if request.user.is_authenticated:
#         return redirect('/')
#     form = LoginForm(request.POST or None)
#     context = {
#         'title': '',
#         'form': form,
#     }
#     if form.is_valid():
#         password = form.cleaned_data.get('password')
#         userName = request.POST['user_name']
#         user = authenticate(request, username=userName, password=password)
#         if user is not None:
#             login(request, user)
#             if request.user.is_authenticated:
#                 data = {
#                     'l': 'python'
#                 }
#                 r = requests.post(url='http://127.0.0.1:8000/login', data=data)
#                 print('r: ', r)
#                 # return redirect('http://127.0.0.1:8000/login')
#                 # return redirect('/')
#         else:
#             form.add_error('user_name', 'رمز یا نام کاربری نادرست است ')
#             form.add_error('password', 'رمز یا نام کاربری نادرست است ')
#
#     return render(request, 'account/login.html', context=context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = LoginForm(request.POST or None)
    context = {
        'title': '',
        'form': form,
    }
    if form.is_valid():
        password = form.cleaned_data.get('password')
        userName = request.POST['user_name']
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                return redirect('/')
        else:
            form.add_error('user_name', 'رمز یا نام کاربری نادرست است ')
            form.add_error('password', 'رمز یا نام کاربری نادرست است ')

    return render(request, 'account/login.html', context=context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'title': '',
        'form': form,
    }

    if form.is_valid():
        userName = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        email = request.POST['email']
        dose_user_exist = User.objects.filter(username=userName).exists()
        if not dose_user_exist:
            User.objects.create_user(username=userName, password=password, email=email)
            return redirect('/login')
        else:
            form.add_error('user_name', "این کاربر با این نام کاربری وجود دارد")

    return render(request, 'account/register.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('/login')
