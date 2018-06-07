# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify
from django.utils.translation import gettext as _

from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFit, ResizeToFill


from rentals.models import Hotel


class Bike(models.Model):
    serial = models.CharField(null=True, blank=True, max_length=50, verbose_name=_('Número de serie'))
    hotel = models.ForeignKey(Hotel, verbose_name=_('Hotel'), related_name='bikes')


    class Meta:
        verbose_name = _('Bici')
        verbose_name_plural = _('Bicis')
        ordering = ['hotel']
