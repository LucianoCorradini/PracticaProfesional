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
    url(r'^login$', accounts.login_view),
    url(r'^logout$', accounts.logout_view),

    url(r'^reservas/nueva/pag1$', app.reservas_nueva_1), # tipo habitacion
    url(r'^reservas/nueva/pag2$', app.reservas_nueva_2), # datos personales
    url(r'^reservas/nueva/pag3$', app.reservas_nueva_3), # reporte final

    url(r'^reservas$', app.reservas), # busqueda y listado
    url(r'^reservas/consultar$', app.reservas_consultar), # busqueda por codigo

    url(r'^reservas/(\d+)$', app.reservas_details), # detalle, edit, delete

    url(r'^habitaciones$', app.habitaciones), # busqueda y listado
    url(r'^habitaciones/nuevo$', app.habitaciones_nuevo), # busqueda y listado
    url(r'^habitaciones/(\d+)$', app.habitaciones_details),
        # detalle, edit, delete

    url(r'^admin/', include(admin.site.urls))
)

