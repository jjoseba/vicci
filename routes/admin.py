# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from routes.models import Category, RoutePoint, HotelRoute, HotelRoutePoint

admin.site.register(Category)
admin.site.register(RoutePoint)
admin.site.register(HotelRoute)
admin.site.register(HotelRoutePoint)