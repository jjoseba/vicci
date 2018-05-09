# coding=utf-8
import datetime
from dateutil.relativedelta import relativedelta
from django import forms

from core.forms.BootstrapModelForm import BootstrapModelForm
from core.models import User
from rentals.models import Hotel


class HotelForm(BootstrapModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'description', 'address', 'photo', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'photo': forms.FileInput(attrs={}),
        }
