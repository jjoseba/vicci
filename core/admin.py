# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from core.models import User, Gallery, GalleryPhoto

admin.site.register(User)


class PhotoInline(admin.TabularInline):
    model = GalleryPhoto

class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryPhoto)