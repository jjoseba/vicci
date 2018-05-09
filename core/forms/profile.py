# coding=utf-8
import datetime
from dateutil.relativedelta import relativedelta
from django import forms

from core.models import User


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'birth_date', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly':True }),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
        }

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        adulthood = datetime.date.today() - relativedelta(years=+18)
        if birth_date and birth_date > adulthood:
            self.add_error('birth_date', u'Hay que ser mayor de edad para utilizar ViCCi')

        return birth_date