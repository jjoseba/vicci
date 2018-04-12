# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from helpers import RandomFileName
from rentals.models import  Hotel
from routes.models import Category, RoutePoint

from django.utils.translation import gettext as _

class HotelRoute(models.Model):

    hotel = models.ForeignKey(Hotel, verbose_name=_('Hotel'), related_name='routes')
    category = models.ForeignKey(Category, verbose_name=_('Categoría'), related_name='hotel_routes')
    points = models.ManyToManyField(RoutePoint, verbose_name=_('Puntos de la ruta'), through='HotelRoutePoint')

    name = models.CharField(null=True, blank=True, verbose_name=_('Nombre'), max_length=250)
    description = models.TextField(null=True, blank=True, verbose_name=_('Descripción'))
    visible = models.BooleanField(default=True, verbose_name=_('Visible'))

    duration = models.IntegerField(default=0, verbose_name=_('Duración de la ruta'))
    distance = models.IntegerField(default=0, verbose_name=_('Distancia de la ruta'))

    photo = ProcessedImageField(null=True, blank=True, upload_to=RandomFileName('momenti/'),
                                verbose_name=_('Imagen principal'),
                                processors=[ResizeToFit(1024, 1024, upscale=False)], format='JPEG')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(150, 150, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 70})

    class Meta:
        verbose_name = _('Momento')
        verbose_name_plural = _('Momentos')
        ordering = ['name']

    def __unicode__(self):
        return self.name if self.name else ''


class HotelRoutePoint(models.Model):

    hotel_route = models.ForeignKey(HotelRoute, verbose_name='Ruta', on_delete=models.CASCADE)
    route_point = models.ForeignKey(RoutePoint, verbose_name='Micromomento', on_delete=models.CASCADE)
    order = models.IntegerField(default=0, verbose_name='Orden')

    class Meta:
        ordering = ['order']
