# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext as _

from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill

from helpers import RandomFileName


class Category(models.Model):

    name = models.CharField(null=True, blank=True, verbose_name=_('Nombre'), max_length=250)
    description = models.TextField(null=True, blank=True, verbose_name=_('Descripción'))
    color = models.CharField(null=True, blank=True, verbose_name=_('Color de etiqueta (código hexadecimal)'), max_length=30)
    photo = ProcessedImageField(null=True, blank=True, upload_to=RandomFileName('momenti/'),
                                verbose_name=_('Imagen principal'),
                                processors=[ResizeToFit(1024, 1024, upscale=False)], format='JPEG')
    photo_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(150, 150, upscale=False)],
                                     format='JPEG',
                                     options={'quality': 70})

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')
        ordering = ['name']

    def __unicode__(self):
        return self.name if self.name else ''
