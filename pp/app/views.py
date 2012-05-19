from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
import json
from django.contrib.auth.models import User, Group
from app.models import Reserva, Habitacion, TipoHabitacion, Persona, TIPOS_DOCUMENTO


def assert_or_404(b):
    if not b:
        raise Http404
    else:
        return b


def index(request):
    # TODO
    return render(request, "index.html")


def reservas_nueva_1(request):
    if request.method == 'GET':
        data = {
            'tipo_habitaciones': TipoHabitacion.objects.all(),
            'msgError': request.GET.get('msgError', None)
        }
        return render(request, "reservas_nueva_pag1.html", data)
    elif request.method == 'POST':
        try:
            # TODO
            return redirect('/reservas/nueva/pag2')
        except:
            return redirect('/reservas/nueva/pag1?msgError="Los datos ingresados son erroneos"')

def reservas_nueva_2(request):
    if request.method == 'GET':
        data = {
            'TIPOS_DOCUMENTO': TIPOS_DOCUMENTO,
            'msgError': request.GET.get('msgError', None)
        }
        return render(request, "reservas_nueva_pag2.html", data)
    elif request.method == 'POST':
        # TODO
        return redirect('/reservas/nueva/pag3')

def reservas_nueva_3(request):
    # TODO
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


