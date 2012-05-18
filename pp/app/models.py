from django.db import models
from django.contrib.auth.models import User

ESTADOS_RESERVA = {
    'en espera': ['atendido', 'cancelado'],
    'atendido': ['cancelado', 'confirmado'],
    'cancelado': [],
    'confirmado': ['cancelado', 'iniciado'],
    'iniciado': ['finalizado', 'arribado', 'cancelado'],
    'arribado': ['finalizado', 'sobrepasado'],
    'sobrepasado': ['finalizado'],
    'finalizado': [],
}

DEFAULT_ESTADO_RESERVA = 'en espera'

ENUMERADO_ESTADOS_RESERVA = [(x, x) for x in ESTADOS_RESERVA.keys()]

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
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s, %s.' % (self.apellido, self.nombre)


class TipoHabitacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default='', null=True, blank=True)
    capacidad = models.PositiveIntegerField(default=2)
    imagen_url = models.SlugField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.nombre


class Habitacion(models.Model):
    numero = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.numero


class Turno(models.Model):
    tiempo_turno = models.PositiveIntegerField()  # en minutos
    entreturno = models.PositiveIntegerField(default=0)  # en minutos
    minimo = models.PositiveIntegerField(null=True, blank=True)  # en cantidad de turnos
    maximo = models.PositiveIntegerField(null=True, blank=True)  # en cantidad de turnos
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # por turno
    tipo_habitacion = models.ForeignKey(TipoHabitacion)


class TurnoHabitacion(models.Model):
    habitacion = models.ForeignKey(Habitacion)
    turno = models.ForeignKey(Turno)


class Reserva(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    estado = models.CharField(max_length=1, choices=ENUMERADO_ESTADOS_RESERVA)
    empresa = models.BooleanField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    creado = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.DecimalField(max_digits=10, decimal_places=2)
    comentario = models.TextField(null=True, blank=True)

    def set_estado(self, estado):
        if estado in ESTADOS_RESERVA[self.estado]:
            self.estado = estado
            return True
        else:
            return False


class SolicitudReserva(models.Model):
    reserva = models.ForeignKey(Reserva)
    turno = models.ForeignKey(Turno)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()


class DetalleReserva(models.Model):
    reserva = models.ForeignKey(Reserva)
    turno_habitacion = models.ForeignKey(TurnoHabitacion)
    inicio = models.DateTimeField()
    fin = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)




