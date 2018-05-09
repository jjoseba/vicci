# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from rentals.models import Hotel, City, Rental

admin.site.register(City)

class HotelAdmin(admin.ModelAdmin):
    list_filter = ('city', )

admin.site.register( Hotel, HotelAdmin)

class RentalAdmin(admin.ModelAdmin):
    list_filter = ('hotel', 'day', 'status')

admin.site.register(Rental, RentalAdmin)