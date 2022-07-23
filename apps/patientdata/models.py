from django.db import models
# from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.timezone import now 
# from phonenumber_field.modelfields import PhoneNumberField

import os, random
# from datetime import date
from string import ascii_uppercase, digits
# import random

current = timezone.now

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "patients/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename)
    


# Create your models here.
class Patients(models.Model):
    name       = models.CharField(max_length=150, unique=True)
    address    = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(default=now, blank=True, null=True)
    age        = models.CharField(max_length=80, blank=True, null=True)
    job        = models.CharField(max_length=80, blank=True, null=True)
    phone      = models.CharField(max_length=150, blank=True, null=True, db_index=True)
    mobile     = models.CharField(max_length=150, blank=True, null=True, db_index=True)
    cardid     = models.CharField(max_length=20, blank=True, null=True, db_index=True)
    barcode    = models.CharField(max_length=100, blank=True, null=True, unique=True)
    barurl     = models.CharField(max_length=200, blank=True, null=True)
    barimg     = models.ImageField(upload_to="patients", null=True, blank=True)


    class Meta:
        db_table = 'patientdata_patients'
        managed = True
        verbose_name = 'patients'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return "{}".format(self.name)

    def edit_patient_url(self):
        # return "/clinic/edit/{}/".format(self.id)
        return reverse('patientdata:edit_patient',
                        kwargs={'id': self.id})



class Operations(models.Model):
    name     = models.CharField(max_length=150, blank=True, null=True, db_index=True)
    opdate   = models.DateField(default=now, blank=True, null=True, db_index=True)
    amount   = models.DecimalField(max_digits=20, decimal_places=2, default=00.00)
    followup = models.CharField(max_length=150, blank=True, null=True)
    improve  = models.CharField(max_length=150, blank=True, null=True)
    heal     = models.BooleanField(default=False)
    remark   = models.CharField(max_length=300, blank=True, null=True)
    patient  = models.ForeignKey(Patients, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id) 

