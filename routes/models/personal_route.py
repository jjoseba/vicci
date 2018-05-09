# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from core.models import User
from rentals.models import Hotel
from routes.models import RoutePoint


class PersonalRoute(models.Model):

    created_by = models.ForeignKey(User, verbose_name=_('Creador'), related_name='personal_routes')
    created = models.DateTimeField(_('Fecha de creación'), default=timezone.now)

    hotel = models.ForeignKey(Hotel, verbose_name=_('Hotel'), related_name='personal_routes')
    points = models.ManyToManyField(RoutePoint, verbose_name=_('Puntos de la ruta'), through='PersonalRoutePoint')
    name = models.CharField(null=True, blank=True, verbose_name=_('Nombre'), max_length=250)
    duration = models.IntegerField(default=0, verbose_name=_('Duración de la ruta'))
    distance = models.IntegerField(default=0, verbose_name=_('Distancia de la ruta'))

    class Meta:
        verbose_name = _('Momento personal')
        verbose_name_plural = _('Momentos personales')
        ordering = ['name']

    def __unicode__(self):
        return self.name if self.name else str(self.hotel)


class PersonalRoutePoint(models.Model):

    hotel_route = models.ForeignKey(PersonalRoute, verbose_name='Ruta', on_delete=models.CASCADE)
    route_point = models.ForeignKey(RoutePoint, verbose_name='Micromomento', on_delete=models.CASCADE)
    order = models.IntegerField(default=0, verbose_name='Orden')

    class Meta:
        ordering = ['order']