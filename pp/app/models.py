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

TIPOS_DOCUMENTO = (
    ('DNI','DNI'),
    ('LC','LC'),
    ('LE','LE'),
    ('CI','CI'),
)


class Persona(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=5, choices=TIPOS_DOCUMENTO)
    numero_documento = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    cuil = models.PositiveIntegerField()
    empresa = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    telefono1 = models.CharField(max_length=20, verbose_name='Telefono')
    telefono2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Tel. alternativo')

    def __unicode__(self):
        return u'%s, %s' % (self.apellido, self.nombre)


class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    es_habitacion = models.BooleanField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_maxima = models.IntegerField()
    duracion_minima = models.IntegerField()
    entreturno = models.TimeField()
    tiempo_turno = models.TimeField()

    def __unicode__(self):
        return self.nombre


class SolicitudReserva(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    empresa = models.BooleanField(default=False)
    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVA)
    fecha_alta = models.DateField(auto_now=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u'Solicitud: %i' % self.id


class ComentarioSolicitudReserva(models.Model):
    reserva = models.ForeignKey(SolicitudReserva)
    usuario = models.ForeignKey(User)
    fecha_hora = models.DateTimeField()
    texto = models.TextField()

    def __unicode__(self):
        return u'%s %s' % ( str(self.fecha_hora), self.texto[:50])


class DetalleSolicitudReserva(models.Model):
    reserva = models.ForeignKey(SolicitudReserva)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    duracion = models.IntegerField(default=1)

    def __unicode__(self):
        return unicode(self.servicio.nombre)


class ServicioDisponible(models.Model):
    servicio = models.ForeignKey(Servicio)
    activo = models.BooleanField(default=True)
    numero = models.PositiveIntegerField()

    def __unicode__(self):
        return u"%s (%d)" % (unicode(self.servicio), self.numero)


class Reserva(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    empresa = models.BooleanField()
    fecha_alta = models.DateField()
#    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVA)

    def __unicode__(self):
        return u"(%s) %s" % (str(self.fecha_alta), unicode(self.cliente))


class DetalleReserva(models.Model):
    reserva = models.ForeignKey(Reserva)
    servicio = models.ForeignKey(ServicioDisponible, on_delete=models.PROTECT)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return u"(%s) %s" % (str(self.inicio), unicode(self.servicio))


class Promocion(models.Model):
    fecha_desde = models.DateField()
    fecha_hasta = models.DateField()
    paquete = models.BooleanField(default=False)
    solo_empresas = models.BooleanField(default=False)

    def __unicode__(self):
        return u''


class DetallePromocion(models.Model):
    promocion = models.ForeignKey(Promocion)
    servicio = models.ForeignKey(Servicio)
    duracion_maxima = models.PositiveIntegerField()
    duracion_minima = models.PositiveIntegerField()
    descuento = models.FloatField()

    def __unicode__(self):
        return u'%s (%d % off)' % (unicode(self.servicio), int(self.descuento))


class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio)
    imagen_url = models.SlugField()
    descripcion = models.TextField()

    def __unicode__(self):
        return self.imagen_url


class Alerta(models.Model):
    reserva = models.ForeignKey(SolicitudReserva)
    usuario = models.ForeignKey(User)
    fecha_hora = models.DateTimeField()
    comentario = models.TextField()

    def __unicode__(self):
        return u'[%s] %s' % (str(self.fecha_hora), self.comentario[:50])




