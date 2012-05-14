from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url
from app import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.index),

    url(r'^reservar$', views.reservar),
    url(r'^datos_personales$', views.datos_personales),
    url(r'^seleccion_servicios$', views.seleccion_servicios),
    url(r'^seleccion_paquetes$', views.seleccion_paquetes),
    url(r'^habitaciones_disponibles$', views.habitaciones_disponibles),

    url(r'^buscar_reserva$', views.buscar_reserva),
    url(r'^servicios_reserva$', views.servicios_reserva),

    url(r'^gestion_habitaciones$', views.gestion_habitaciones),
    url(r'^gestion_servicios$', views.gestion_servicios),
    url(r'^gestion_promociones$', views.gestion_promociones),
    url(r'^gestion_paquetes$', views.gestion_paquetes),

    url(r'login/$', 'django.contrib.auth.views.login'),
    url(r'logout/$', 'django.contrib.auth.views.logout'),

    url(r'^admin/', include(admin.site.urls)),
)

