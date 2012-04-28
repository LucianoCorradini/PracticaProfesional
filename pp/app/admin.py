import app.models
from django.contrib import admin
#from django.contrib.contenttypes import generic


class AdminPersona(admin.ModelAdmin):
    fieldsets = [
        ('Persona', {'fields': ['user', ('apellido', 'nombre'), 'fecha_nacimiento']}),
        (None, {'fields': [('tipo_documento', 'numero_documento')]}),
        ('Laboral', {'fields': [('cuil', 'empresa')]}),
        ('Contacto', {'fields': ['email', 'telefono1', 'telefono2']})
    ]

admin.site.register(app.models.Persona, AdminPersona)


class DetalleSolicitudReservaInline(admin.TabularInline):
    model = app.models.DetalleSolicitudReserva


class ComentarioSolicitudReservaInline(admin.TabularInline):
    model = app.models.ComentarioSolicitudReserva


class AdminSolicitudReserva(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['cliente', ('empresa', 'estado', 'monto')]})
    ]
    inlines = [
        DetalleSolicitudReservaInline, ComentarioSolicitudReservaInline
    ]

admin.site.register(app.models.SolicitudReserva, AdminSolicitudReserva)


class DetalleReservaInline(admin.TabularInline):
    model = app.models.DetalleReserva


class AdminReserva(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['cliente', 'empresa', 'fecha_alta']})
    ]
    inlines = [
        DetalleReservaInline,
    ]

admin.site.register(app.models.Reserva, AdminReserva)


class ServicioDisponibleInline(admin.TabularInline):
    model = app.models.ServicioDisponible


class ImagenServicioInline(admin.TabularInline):
    model = app.models.ImagenServicio


class AdminServicio(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('nombre', 'capacidad', 'precio', 'es_habitacion'),('duracion_minima', 'tiempo_turno', 'duracion_maxima', 'entreturno')]})
    ]
    inlines = [
        ServicioDisponibleInline, ImagenServicioInline,
    ]

admin.site.register(app.models.Servicio, AdminServicio)


class DetallePromocionInline(admin.TabularInline):
    model = app.models.DetallePromocion


class AdminPromocion(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': [('fecha_desde', 'fecha_hasta'), ('paquete', 'solo_empresas')]})
    ]
    inlines = [
        DetallePromocionInline
    ]

admin.site.register(app.models.Promocion, AdminPromocion)





