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

ESTADOS_SERVICIO = (
    ('D', 'Disponible'),
    ('N', 'No Disponible'),
    ('U', 'En Uso'),
)

TIPOS_DOCUMENTO = (
    ('DNI', 'DNI'),
    ('LC', 'LC'),
    ('LE', 'LE'),
    ('CI', 'CI'),
)


class Persona(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.SET_NULL)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    tipo_documento = models.CharField(max_length=5, choices=TIPOS_DOCUMENTO)
    numero_documento = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    empresa = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    telefono1 = models.CharField(max_length=20, verbose_name='Telefono')
    telefono2 = models.CharField(max_length=20, null=True, blank=True,
                                 verbose_name='Tel. alternativo')

    def __unicode__(self):
        return u'%s, %s.' % (self.apellido, self.nombre)


class SolicitudReserva(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    comentario = models.TextField()

#    def __unicode__(self):
#        return (self.cliente.__unicode__() +
#               u" , Solicitud %s" % (self.id))


class Reserva(models.Model):
    solicitud = models.ForeignKey(SolicitudReserva, on_delete=models.PROTECT)
    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVA)
    empresa = models.BooleanField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    creado = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField()

#    def __unicode__(self):
#        return (self.solicitud.cliente.__unicode__() +
#               u" , Reserva %s" % (self.id))


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveIntegerField()
    imagen_url = models.SlugField()
    descripcion = models.TextField()

    def __unicode__(self):
        return unicode(self.nombre)


class Caracteristica(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __unicode__(self):
        return unicode(self.nombre)


class Habitacion(models.Model):
    numero = models.PositiveIntegerField()
    caracteristicas = models.ManyToManyField(Caracteristica)

    def __unicode__(self):
        return unicode(self.numero)


class TipoServicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.SlugField()

    def __unicode__(self):
        return unicode(self.nombre)


class Servicio(models.Model):
    numero = models.PositiveIntegerField()
    estado = models.CharField(max_length=1, choices=ESTADOS_SERVICIO)
    tipo = models.ForeignKey(TipoServicio)

    def __unicode__(self):
        return u"%s %s" % (self.tipo.nombre, self.numero)


class Turno(models.Model):
    tiempo_turno = models.DateTimeField()
    minimo = models.PositiveIntegerField()
    maximo = models.PositiveIntegerField()

#    def __unicode__(self):
#        return unicode(self.id)


class TurnoServicio(Turno):
    servicio = models.ForeignKey(Servicio)

#    def __unicode__(self):
#        return


class TurnoHabitacion(Turno):
    habitacion = models.ForeignKey(Habitacion)

#    def __unicode__(self):
#        return


class DetalleReserva(models.Model):
    reserva = models.ForeignKey(Reserva)
    fechahora = models.DateTimeField()  # de llegada perhaps??
    turnos = models.PositiveIntegerField()  # pondria llegada y salida
    monto = models.DecimalField(max_digits=10, decimal_places=2)

#    def __unicode__(self):
#        return


class DetalleReservaHabitacion(DetalleReserva):
    habitacion = models.ForeignKey(Habitacion)
    turno = models.ForeignKey(TurnoHabitacion)

#    def __unicode__(self):
#        return


class DetalleReservaServicio(DetalleReserva):
    servicio = models.ForeignKey(Servicio)
    turno = models.ForeignKey(TurnoServicio)

#    def __unicode__(self):
#        return





