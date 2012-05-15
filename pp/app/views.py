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

##########################
#- UI Registrar Reserva -#
##########################


def reservar(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("/datos_personales")
    return render(request, "reservar.html")


def seleccion_servicios(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/reservar")
        else:
            return redirect("/datos_personales")
    return render(request, "seleccion_servicios.html")


def seleccion_paquetes(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/reservar")
        else:
            return redirect("/datos_personales")
    return render(request, "seleccion_paquetes.html")


def datos_personales(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/reservar")
    return render(request, "datos_personales.html")


def habitaciones_disponibles(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/reservar")
    return render(request, "habitaciones_disponibles.html")


#######################
#- UI Buscar Reserva -#
#######################


def buscar_reserva(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("buscar_reserva")
    return render(request, "buscar_reserva.html")


def servicios_reserva(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("servicios_reserva")
    return render(request, "servicios_reserva.html")


#######################
#-  UI  Admin Hotel  -#
#######################


def gestion_habitaciones(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("gestion_habitaciones")
    return render(request, "gestion_habitaciones.html")


def gestion_servicios(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("gestion_servicios")
    return render(request, "gestion_servicios.html")


def gestion_promociones(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("gestion_promociones")
    return render(request, "gestion_promociones.html")

def gestion_paquetes(request):
    if request.method == "POST":
        if request.POST["commit"] == "cancelar":
            return redirect("/")
        else:
            return redirect("gestion_paquetes")
    return render(request, "gestion_paquetes.html")

