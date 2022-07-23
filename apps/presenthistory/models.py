from django.db import models
from django.shortcuts import reverse
from datetime import date
from apps.patientdata.models import Patients
from apps.visits.models import Visits



# Create your models here.



class PresentHistory(models.Model):
    visitdate    = models.DateField(default=date.today, blank=True, null=True)
    temprature = models.DecimalField(decimal_places=2,
                                max_digits=5,
                                default=00.00,
                                blank=True)
    weight = models.DecimalField(decimal_places=2,
                                max_digits=5,
                                default=000.00,
                                blank=True)
    height = models.DecimalField(decimal_places=2,
                                max_digits=5,
                                default=000.00,
                                blank=True)
    cholestrol   = models.CharField(max_length=150, null=True, blank=True)
    pulse        = models.CharField(max_length=150, null=True, blank=True)
    bloodpr      = models.CharField(max_length=150, null=True, blank=True)
    bsl          = models.CharField(max_length=150, null=True, blank=True)
    hb           = models.CharField(max_length=150, null=True, blank=True)
    patient      = models.ForeignKey(Patients, null=True, blank=True, on_delete=models.CASCADE)
    visit        = models.ForeignKey(Visits, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id)

    def get_presenthistory_url(self):
        return reverse('patientdata:save_present_hist',
                kwargs={'patient_id': self.patient, 'visit':self.visit})

    # def get_visit_url(self):
    #     return reverse('clinic:visits_patient_id',
    #                     kwargs={'id':self.id, 'patient':self.patient})
