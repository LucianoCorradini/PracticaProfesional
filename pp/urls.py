from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url

from app import views as app
from accounts import views as accounts

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', app.index),
    url(r'^index$', app.index),

    # user login / logout
    url(r'^login$', account.login),
    url(r'^logout$', account.logout),

    url(r'^reservas/nueva/pag1$', app.reservas_nueva_1), # tipo habitacion
    url(r'^reservas/nueva/pag2$', app.reservas_nueva_2), # servicios
    url(r'^reservas/nueva/pag3$', app.reservas_nueva_3), # datos personales

    url(r'^reservas$', app.reservas), # busqueda y listado
    url(r'^reservas/consultar$', app.reservas_consultar), # busqueda por codigo

    url(r'^reservas/(\d+)$', app.reservas_id), # detalle, edit, delete

    url(r'^habitaciones$', app.habitaciones), # busqueda y listado
    url(r'^habitaciones/(\d+)$', app.habitaciones_id), # detalle, edit, delete

    url(r'^admin/', include(admin.site.urls))
)

