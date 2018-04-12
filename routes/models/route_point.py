# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _

from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from helpers import RandomFileName
from rentals.models import City
from routes.models import Category


class RoutePoint(models.Model):

    city = models.ForeignKey(City, verbose_name=_('Ciudad'), related_name='points')
    category = models.ForeignKey(Category, verbose_name=_('Categoría'), related_name='points')
    name = models.CharField(null=True, blank=True, verbose_name=_('Nombre'), max_length=250)
    description = models.TextField(null=True, blank=True, verbose_name=_('Descripción'))
    latitude = models.FloatField(null=False, verbose_name=_('Latitud'), default=0)
    longitude = models.FloatField(null=False, verbose_name=_('Longitud'), default=0)
    photo = ProcessedImageField(null=True, blank=True, upload_to=RandomFileName('momenti/'),
                                verbose_name=_('Imagen principal'),
                                processors=[ResizeToFit(1024, 1024, upscale=False)], format='JPEG')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(150, 150, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 70})


    class Meta:
        verbose_name = 'Micromomento'
        verbose_name_plural = 'Micromomentos'
        ordering = ['name']

    def __unicode__(self):
        return self.name if self.name else ''
