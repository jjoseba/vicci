# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-08 17:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentals', '0002_auto_20180322_0024'),
        ('routes', '0002_hotel_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRoute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creaci\xf3n')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('duration', models.IntegerField(default=0, verbose_name='Duraci\xf3n de la ruta')),
                ('distance', models.IntegerField(default=0, verbose_name='Distancia de la ruta')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_routes', to=settings.AUTH_USER_MODEL, verbose_name='Creador')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_routes', to='rentals.Hotel', verbose_name='Hotel')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Momento personal',
                'verbose_name_plural': 'Momentos personales',
            },
        ),
        migrations.CreateModel(
            name='PersonalRoutePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0, verbose_name='Orden')),
                ('hotel_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.PersonalRoute', verbose_name='Ruta')),
                ('route_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.RoutePoint', verbose_name='Micromomento')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AlterField(
            model_name='hotelroutepoint',
            name='hotel_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.HotelRoute', verbose_name='Ruta'),
        ),
        migrations.AddField(
            model_name='personalroute',
            name='points',
            field=models.ManyToManyField(through='routes.PersonalRoutePoint', to='routes.RoutePoint', verbose_name='Puntos de la ruta'),
        ),
    ]
