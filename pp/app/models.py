from django.db import models
from django.contrib.auth.models import User

ESTADOS_RESERVA = (
    ('A', 'Activa'),
    ('C', 'Completa'), # Se realizo con exito
    ('X', 'Cancelada'),
    ('P', 'Pendiente'), # falta la totalidad del pago
)


class Persona(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # relacion 1 a 1, 0-1, 1-0 chequear
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    cuil = models.IntegerField()
    email = models.EmailField()
    empresa = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    numero_documento = models.IntegerField()
    #le pongo a todo 50 aunque seguramente el max length telefonos y tipo documento sea menor
    tipo_documento = models.CharField(max_length=50)
    telefono1 = models.CharField(max_length=50)
    telefono2 = models.CharField(max_length=50)
    #faltaria agregar el unique "numero_documento + tipo_documento"

    def __unicode__(self):
        return u'Persona: %s, %s\n Documento: %s, %i\n' % (self.apellido, self.nombre, self.tipo_documento, self.numero_documento)


class SolicitudReserva(models.Model):

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    empresa = models.BooleanField()#tambien podria ser NullBooleanField
    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVA)
    fecha_alta = models.DateField(auto_now=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'Solicitud de Reserva Numero: %i\n Cliente: %i\n Fecha de Alta: %s\n Monto Abonado: %f\n Estado: %s\n' % (self.id, self.cliente, self.fecha_alta, self.monto, self.estado)


class Alerta(models.Model):

    id = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(SolicitudReserva, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(User)
    fecha_hora = models.DateTimeField()
    comentario = models.CharField(max_length=100)

    def __unicode__(self):
        return u'Alerta Numero: %i\n  Usuario: %i\n  Reserva: %i\n  Fecha y Hora: %s\n  Comentario: %s\n' % (self.id, self.usuario, self.reserva, self.fecha_hora, self.comentario)


class ComentarioReserva(models.Model):

    id = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(SolicitudReserva, on_delete=models.CASCADE)
    usuario = models.ManyToManyField(User)
    comentario = models.TextField()

    def __unicode__(self):
        return u'id: %i\n  Usuario: %i\n  Reserva: %i\n  Comentario: %s\n' % (self.id, self.usuario, self.reserva, self.comentario)


class Reserva(models.Model):

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    empresa = models.BooleanField()
    fecha_alta = models.DateField()
#no esta clara la relacion entre Reserva y SolicitudReserva , tendria que haber una FK de SolicitudReserva a Reserva?

    def __unicode__(self):
        return u'Reserva: %i\n  Cliente: %i\n  Fecha de alta: %s\n  Empresa: %s\n' % (self.id, self.cliente, self.fecha_hora, self.empresa)


class Servicio(models.Model):

    id = models.AutoField(primary_key=True)
    capacidad = models.IntegerField()
    duracion_maxima = models.TimeField()#Era int en modelo logico
    duracion_minima = models.TimeField()#Era int en modelo logico
    entreturno = models.TimeField()#Era int en modelo logico
    es_habitacion = models.BooleanField()
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_turno = models.TimeField()#Era int en modelo logico

    def __unicode__(self):
        return u'Servicio: %i, %s\n Precio: %10d.%02d\n  Capacidad: %i\n Tiempo del Turno: %s\n  Duracion Maxima: %s\n  Duracion Minima: %s\n  Entre Turno: %s\n Es Habitacion: %s\n  ' % (self.id, self.nombre, self.precio, self.capacidad, self.tiempo_turno, self.duracion_maxima, self.duracion_minima, self.entreturno, self.es_habitacion)


class DetalleSolicitudReserva(models.Model):

    id = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(SolicitudReserva,on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)

    def __unicode__(self):
        return u'Detalle Solicitud Reserva: %i, Reserva: %i, Servicio: %i.\n' % (self.id, self.reserva, self.servicio)


class ImagenServicio(models.Model):

    id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)
    imagen_url = models.SlugField()
    descripcion = models.TextField()

    def __unicode__(self):
        return u'Imagen del servicio: %i, Servicio: %i, URL: %i.\n Descripcion: %s\n' % (self.id, self.servicio, self.imagen_url, self.descripcion)


class ServicioDisponible(models.Model):

    id = models.AutoField(primary_key=True)
    servicio = models.ForeignKey(Servicio,on_delete=models.PROTECT)
    activo = models.BooleanField()
    numero = models.IntegerField()

    def __unicode__(self):
        return u'Servicio Disponible: %i, Servicio: %i, Activo: %s, Numero: %i\n' % (self.id, self.servicio, self.activo, self.numero)


#en DetalleReserva supongo que tiene que estar relacionado con la reserva en si, lo cual lleva al cliente que la tiene y no tengo FK cliente
class DetalleReserva(models.Model):

    id = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(Reserva,on_delete=models.PROTECT)
    servicio = models.ForeignKey(ServicioDisponible,on_delete=models.PROTECT)
    fin = models.DateField() #falta especificar en el modelo logico
    inicio = models.DateField() #falta especificar en el modelo logico
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'Reserva: %i, Detalle Reserva: %i, Servicio: %i\n Inicio: %s, Finalizacion: %s\n Monto: %f, Pagado: %f\n' % (self.reserva, self.id, self.servicio, self.inicio, self.fin, self.monto, self.pagado)


class Promocion(models.Model):

    id = models.AutoField(primary_key=True)
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    paquete = models.BooleanField()
    solo_empresas = models.BooleanField()

    def __unicode__(self):
        return u'Promocion: %i, Fecha de Comienzo: %s, Fecha de Finalizacion: %s, Paquete: %s, Solo Empresas: %s\n' % (self.id, self.fecha_desde, self.fecha_hasta, self.paquete, self.solo_empresas)


class DetallePromocion(models.Model):

    id = models.AutoField(primary_key=True)
    promocion = models.ForeignKey(Promocion, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    duracion_maxima = models.TimeField()#Era int en modelo logico
    duracion_minima = models.TimeField()#Era int en modelo logico
    descuento = models.FloatField()

    def __unicode__(self):
        return u'Promocion: %i, Detalle: %i, Servicio: %i, Duracion Maxima: %s, Duracion Minima: %s, descuento: %f\n' % (self.promocion, self.id, self.servicio, self.duracion_maxima, self.duracion_minima, self.descuento)
