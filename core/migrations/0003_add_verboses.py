# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-08 17:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_gallery_galleryphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="El tel\xe9fono debe tener el formato: '+999999999'. Hasta 15 d\xedgitos permitidos.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Tel\xe9fono'),
        ),
    ]
