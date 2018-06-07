# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _

from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from core.models import Gallery, User
from helpers import RandomFileName
from rentals.models import City, Hotel, Bike

STATUS_ACCEPTED = 'accepted'
STATUS_CANCELLED = 'cancelled'
STATUS_OVERDUE = 'overdue'
STATUS_CHECKIN = 'checkin'
STATUS_CHECKOUT = 'checkout'
PAYMENT_STATUS = (
    (STATUS_ACCEPTED, 'Aceptado'),
    (STATUS_CANCELLED, 'Cancelado'),
    (STATUS_OVERDUE, 'Pasado'),
    (STATUS_CHECKIN, 'Retirada'),
    (STATUS_CHECKOUT, 'Devuelta'),
)

class Rental(models.Model):

    client = models.ForeignKey(User, verbose_name=_('Cliente'), blank=True, null=True, related_name='rentals')
    hotel = models.ForeignKey(Hotel, verbose_name=_('Hotel'), related_name='rentals')
    timestamp = models.DateTimeField(verbose_name=_('Realizada'), default=timezone.now)
    is_guest = models.BooleanField(default=False, verbose_name=_('Es cliente del hotel'))
    room_number = models.CharField(null=True, blank=True, verbose_name=_('Habitación'), max_length=100)
    day = models.DateField(verbose_name=_('Dia de reserva'))
    time = models.TimeField(verbose_name=_('Hora de recogida'))
    duration = models.DurationField(default=0, verbose_name=_('Duración'))
    status = models.CharField(max_length=12, choices=PAYMENT_STATUS, verbose_name=_('Estado'))
    total_amount = models.FloatField(default=0, verbose_name='Importe total')
    day_complete = models.BooleanField(default=False, verbose_name=_('Día completo'))


    class Meta:
        verbose_name = _('Reserva')
        verbose_name_plural = _('Reservas')
        ordering = ['day', 'time']


    def __unicode__(self):
        return self.hotel.name + ' | ' + str(self.day) + ' - ' + str(self.time)


class RentalBike(models.Model):

    rental = models.ForeignKey(Rental, verbose_name=_('Reserva'), blank=False, null=False, related_name='bikes')
    full_name = models.TextField(null=False, blank=False, verbose_name=_('Nombre completo'))
    nif = models.CharField(null=False, blank=False, max_length=20, verbose_name=_('DNI/NIF'))
    birthdate = models.DateField(null=False, blank=False, verbose_name=_('Fecha de nacimiento'))
    bike = models.ForeignKey(Bike, null=False, related_name='rentals')


    class Meta:
        verbose_name = _('Persona reserva')
        verbose_name_plural = _('Personas reserva')
