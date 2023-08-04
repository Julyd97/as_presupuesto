from django.db import models
from user.models import User, UserBase
# Create your models here.

class School(UserBase):
    dane_code = models.CharField(('dane code'), max_length=100)
    cont_menor_cuantia = models.CharField(('contratacion menor cuantia'), max_length=30, blank=True)
    cont_minima_cuantia = models.CharField(('contratacion minima cuantia'), max_length=30, blank=True)
    institutional_mail = models.EmailField(('institutional mail'), null=True)
    address = models.CharField(('address'), max_length=30)
    date_acuerdos =  models.DateField(('date acuerdos'), blank=True)
    date_resolucion = models.DateField(('date resolucion'), blank=True)
    lema = models.CharField(('lema'), max_length=120)
    localidad = models.CharField(('localidad'), max_length=20)
    cellphone = models.IntegerField(('cellphone'))
    phone = models.IntegerField(('phone'))

    def school_mail(self):
        '''
        get school mail
        '''
        return self.institutional_mail

    def school_dane(self):
        '''
        get dane code of the school
        '''
        return self.dane_code