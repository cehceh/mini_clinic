from django.db import models
from django.urls import reverse
from django.utils.timezone import timezone
from datetime import date
from string import ascii_uppercase, digits
import random

from apps.patientdata.models import Patients
from apps.visits.models import Visits


# Create your models here.

class Revisits(models.Model):
    visitdate    = models.DateField(default=date.today, blank=True, null=True)
    complain     = models.TextField(blank=True, null=True)
    sign         = models.TextField(null=True, blank=True)
    diagnosis    = models.CharField(max_length=150, null=True, blank=True)
    intervention = models.CharField(max_length=150, null=True, blank=True)
    amount       = models.IntegerField(default=0, blank=True)
    patient      = models.ForeignKey(Patients, null=True, blank=True, on_delete=models.CASCADE)
    visit        = models.ForeignKey(Visits, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id)

    def get_url(self):
        return reverse('revisitdata:save_revisit', 
                        kwargs={'patient':self.patient_id, 'visit':self.visit})


