from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group


def assert_or_404(b):
    if not b:
        raise Http404
    else:
        return b


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    
    # TODO: logiar usuario y pass.
    return redirect("/")


def logout(request):
    # TODO: deslogiar usuario y pass.
    return redirect("/")


