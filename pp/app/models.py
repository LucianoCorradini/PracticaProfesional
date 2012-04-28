from django.db import models
from django.contrib.auth.models import User

ESTADOS_RESERVA = (
    ('A', 'Activa'),
    ('R', 'Rechazada'),
    ('E', 'En Espera'),
    ('X', 'En Curso'),
    ('F', 'Finalizada'),
    ('C', 'Completada'),
)


class Persona(models.Model):

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=5)
    numero_documento = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()#habra que validar
    cuil = models.PositiveIntegerField()
    empresa = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    telefono1 = models.CharField(max_length=20)
    telefono2 = models.CharField(max_length=20, null=True, blank=True)
    #faltaria agregar el unique "numero_documento + tipo_documento"

    def __unicode__(self):
        return u'Persona: %s, %s\n Documento: %s, %i\n' % (self.apellido, self.nombre, self.tipo_documento, self.numero_documento)


class Servicio(models.Model):

    capacidad = models.PositiveIntegerField()
    duracion_maxima = models.PositiveIntegerField()
    duracion_minima = models.PositiveIntegerField()
    entreturno = models.PositiveIntegerField()
    es_habitacion = models.BooleanField()
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_turno = models.IntegerField()
    timeDelta = models.TimeField()#todavia no definido

    def __unicode__(self):
        return u'Servicio: %i, %s\n Precio: %f\n  Capacidad: %i\n Duracion: ( %i, %i, %i )\n' % (self.id, self.nombre, self.precio, self.capacidad, self.duracion_maxima,self.tiempo_turno, self.duracion_minima)


class SolicitudReserva(models.Model):

    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    empresa = models.BooleanField()#tambien podria ser NullBooleanField
    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVA)
    fecha_alta = models.DateField(auto_now=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    alertas = models.ManyToManyField(User, through='Alerta')
    #Hago que los comentarios no sean M2M por conflicto con alertas
    #comentarios = models.ManyToManyField(User, through='ComentarioSolicitudReserva')
    detalles = models.ManyToManyField(Servicio, through='DetalleSolicitudReserva')


    def __unicode__(self):
        return u'Solicitud: %i\n Cliente: %i\n Alta: %s\n Monto Abonado: %f\n Estado: %s\n' % (self.id, self.cliente, self.fecha_alta, self.monto, self.estado)


class Alerta(models.Model):

    reserva = models.ForeignKey(SolicitudReserva)
    usuario = models.ForeignKey(User)
    fecha_hora = models.DateTimeField()
    comentario = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Reserva: %i\n  Activacion: %s\n  Comentario: %s\n' % ( self.reserva, self.fecha_hora, self.comentario)


class ComentarioSolicitudReserva(models.Model):

    reserva = models.ForeignKey(SolicitudReserva)
    comentario = models.TextField()

    def __unicode__(self):
        return u'id: %i\n  Reserva: %i\n  Comentario: %s\n' % (self.id, self.reserva, self.comentario)



class DetalleSolicitudReserva(models.Model):

    reserva = models.ForeignKey(SolicitudReserva,on_delete=models)
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)

    def __unicode__(self):
        return u'Detalle Solicitud Reserva: %i, Reserva: %i, Servicio: %i.\n' % (self.id, self.reserva, self.servicio)


class ServicioDisponible(models.Model):

    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)
    activo = models.BooleanField()
    numero = models.PositiveIntegerField()

    def __unicode__(self):
        return u'Servicio: %s, %i, Activo: %s\n' % (self.servicio.nombre,self.numero, self.activo)


class Reserva(models.Model):

    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    empresa = models.BooleanField()
    fecha_alta = models.DateField()
    detalles = models.ManyToManyField(ServicioDisponible, through='DetalleReserva')

    def __unicode__(self):
        return u'Reserva: %i\n  Cliente: %i\n  Alta: %s\n  Empresa: %s\n' % (self.id, self.cliente, self.fecha_hora, self.empresa)


class ImagenServicio(models.Model):

    servicio = models.ForeignKey(Servicio)
    imagen_url = models.SlugField()
    descripcion = models.TextField()

    def __unicode__(self):
        return u'Imagen del servicio: %i, Servicio: %i, URL: %i.\n' % (self.id, self.servicio, self.imagen_url)


class DetalleReserva(models.Model):

    reserva = models.ForeignKey(Reserva,on_delete=models.PROTECT)
    servicio = models.ForeignKey(ServicioDisponible,on_delete=models.PROTECT)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'Reserva: %i, Servicio: %i\n Inicio: %s, Fin: %s\n Monto: %f, Pagado: %f\n' % (self.reserva, self.servicio, self.inicio, self.fin, self.monto, self.pagado)


class Promocion(models.Model):

    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    paquete = models.BooleanField()
    solo_empresas = models.BooleanField()
    detalles = models.ManyToManyField(Servicio, through='DetallePromocion')

    def __unicode__(self):
        return u'Promocion: %i, Comienzo y Finalizacion: %s, %s\n' % (self.id, self.fecha_desde, self.fecha_hasta)


class DetallePromocion(models.Model):

    promocion = models.ForeignKey(Promocion)
    servicio = models.ForeignKey(Servicio)
    duracion_maxima = models.PositiveIntegerField()
    duracion_minima = models.PositiveIntegerField()
    descuento = models.FloatField()
    timeDelta = models.TimeField()#todavia no definido

    def __unicode__(self):
        return u'Promocion: %i, Servicio: %i, Duracion: (%i, %i), descuento: %f\n' % (self.promocion, self.servicio, self.duracion_maxima, self.duracion_minima, self.descuento)




