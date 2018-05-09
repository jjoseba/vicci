# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


from routes.models import Category, RoutePoint, HotelRoute, HotelRoutePoint, PersonalRoute
from django.utils.translation import ugettext, ugettext_lazy as _

class RoutePointInline(admin.TabularInline):
    model = HotelRoutePoint
    verbose_name = _("Punto de la ruta")
    verbose_name_plural = _("Puntos de la ruta")

class RoutePointAdmin(admin.ModelAdmin):
    list_filter = ('city', 'category')
    list_display = ['name', 'city', 'category', ]


class HotelRouteAdmin(admin.ModelAdmin):
    list_filter = ('hotel', 'category')
    list_display = ('name', 'hotel', 'category', )
    inlines = [
        RoutePointInline,
    ]


admin.site.register(Category)
admin.site.register(HotelRoute, HotelRouteAdmin)
admin.site.register(HotelRoutePoint)

admin.site.register( RoutePoint, RoutePointAdmin)

admin.site.register( PersonalRoute )