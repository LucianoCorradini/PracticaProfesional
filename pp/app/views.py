from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.db import transaction
import json


def assert_or_404(b):
    if not b:
        raise Http404
    else:
        return b


def index(request):
    return render(request, "index.html")


def reservar(request):
    if request.method == "POST":
        if request.POST["commit"]=="cancelar":
            return redirect("/")
        else:
            return redirect("/datos_personales")
    return render(request, "reservar.html")


def datos_personales(request):
    if request.method == "POST":
        if request.POST["commit"]=="cancelar":
            return redirect("/")
    return render(request, "datos_personales.html")

