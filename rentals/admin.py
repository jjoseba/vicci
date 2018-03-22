# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from rentals.models import Hotel, City


admin.site.register(City)
admin.site.register(Hotel)