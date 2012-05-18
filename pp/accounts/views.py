from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout


def assert_or_404(b):
    if not b:
        raise Http404
    else:
        return b


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")  # success!
            else:
                return redirect("/")  # disabled account!
    else:
        return redirect("/")  # invalid login!

def logout_view(request):
    logout(request)
    return redirect("/")


