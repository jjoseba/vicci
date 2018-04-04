# coding=utf-8
import datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth.forms import UserCreationForm
from django import forms

from core.models import User


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ("username", 'email', 'birth_date', 'phone_number', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control datepicker'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            self.add_error('username', u'El nombre de usuario "%s" ya está en uso.' % username)
        return username

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        adulthood = datetime.date.today() - relativedelta(years=+18)

        if birth_date > adulthood:
            pass
            # self.add_error('birth_date', u'Hay que ser mayor de edad para utilizar ViCCi')

        return birth_date