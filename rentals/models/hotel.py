# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext as _

from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from core.models import Gallery, User
from helpers import RandomFileName
from rentals.models import City


class Hotel(models.Model):

    owner = models.ForeignKey(User, verbose_name=_('Responsable'), blank=True, null=True, related_name='hotels')
    city = models.ForeignKey(City,verbose_name=_('Ciudad'), related_name='hotels')
    name = models.CharField(null=True, blank=True, verbose_name=_('Nombre'), max_length=250)
    description = models.TextField(null=True, blank=True, verbose_name=_('Descripción'))
    address = models.TextField(null=True, blank=True, verbose_name=_('Dirección'))
    latitude = models.FloatField(null=False, verbose_name=_('Latitud'), default=0)
    longitude = models.FloatField(null=False, verbose_name=_('Longitud'), default=0)
    photo = ProcessedImageField(null=True, blank=True, upload_to=RandomFileName('cities/'),
                                verbose_name=_('Imagen principal'),
                                processors=[ResizeToFit(1024, 1024, upscale=False)], format='JPEG')
    photo_thumbnail = ImageSpecField(source='photo',
                                       processors=[ResizeToFill(150, 150, upscale=False)],
                                       format='JPEG',
                                       options={'quality': 70})

    gallery = models.OneToOneField(Gallery, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hoteles')
        ordering = ['name']

    def __unicode__(self):
        return self.name
