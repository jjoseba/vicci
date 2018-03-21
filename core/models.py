# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import gettext as _

from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message=_("El teléfono debe tener el formato: '+999999999'. Hasta 15 dígitos permitidos."))
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
