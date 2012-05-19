from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
import json
from django.contrib.auth.models import User, Group
from app.models import Reserva, Habitacion, TipoHabitacion, Persona


def assert_or_404(b):
    if not b:
        raise Http404
    else:
        return b


def index(request):
    data = {
        'index_data': TipoHabitacion.objects.all(),
        'msgError': request.GET.get('msgError', None)
    }
    return render(request, "index.html", data)


def reservas_nueva_1(request):
    if request.method == 'GET':
        data = {
            'tipo_habitaciones': TipoHabitacion.objects.all(),
            'msgError': request.GET.get('msgError', None)
        }
        return render(request, "reservas_nueva_pag1.html", data)
    elif request.method == 'POST':
        try:
            return redirect('/reservas/nueva/pag2')
        except:
            return redirect('/reservas/nueva/pag1?msgError="Los datos ingresados son erroneos"')

def reservas_nueva_2(request):
    if request.method == 'GET':
        data = {
            'msgError': request.GET.get('msgError', None)
        }
        return render(request, "reservas_nueva_pag2.html")
    elif request.method == 'POST':
        # TODO
        return redirect('/reservas/nueva/pag3')

def reservas_nueva_3(request):
    if request.method == 'GET':
#        data = {
#            'id_reserva':
#            'msgError': request.GET.get('msgError', None)
#        }
        return render(request, "reservas_nueva_pag3.html")



def reservas(request):
    assert_or_404(user.is_staff)
    if request.method == 'GET':
        # TODO
        return render(request, "reservas.html")
    elif request.method == 'POST':
        # TODO
        return render(request, "reservas.html")

def reservas_consultar(request):
    if request.method == 'GET':
        # TODO
        return render(request, "reservas_consultar.html")
    elif request.method == 'POST':
        # TODO
        return redirect('/reservas/%d' + int(pk))

def reservas_details(request, pk):
    get_object_or_404(Reserva, pk=int(pk))
    if request.method == 'GET':
        # TODO
        return render(request, "reservas_details.html")
    elif request.method == 'POST':
        # TODO
        return render(request, "reservas_details.html")
    elif request.method == 'DELETE':
        # TODO
        return redirect(request, 'index')


def habitaciones(request):
    if request.method == 'GET':
        # TODO
        return render(request, "habitaciones.html")
    elif request.method == 'POST':
        # TODO
        return render(request, "habitaciones.html")

def habitaciones_nuevo(request):
    if request.method == 'GET':
        # TODO
        return render(request, "habitaciones_nuevo.html")
    elif request.method == 'POST':
        # TODO
        return redirect(request, 'habitaciones')

def habitaciones_details(request, pk):
    get_object_or_404(Reserva, pk=int(pk))
    if request.method == 'GET':
        # TODO
        return render(request, "reservas_details.html")
    elif request.method == 'POST':
        # TODO
        return render(request, "reservas_details.html")
    elif request.method == 'DELETE':
        # TODO
        return redirect(request, 'index')


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

