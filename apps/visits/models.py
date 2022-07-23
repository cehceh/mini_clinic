from django.db import models
from django.urls import reverse
from django.utils.timezone import timezone
from datetime import date
from string import ascii_uppercase, digits
import random
from apps.patientdata.models import Patients
# from apps.patientdata.models import Patients
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from django.contrib.postgres.search import SearchVector
#
def validate_none(value):
    if value == None:
        raise ValidationError(_('%(value)s must be not NONE'),
            params={'value': '0'},
        )

# Sample of an ID generator - could be any string/number generator
# For a 6-char field, this one yields 2.1 billion unique IDs
def id_generator(size=6, chars=ascii_uppercase + digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Visits(models.Model):
    patient = models.ForeignKey(Patients, null=True, blank=True, on_delete=models.CASCADE)
    visitdate = models.DateField(default=date.today, blank=True, null=True)
    complain = models.TextField(default="comp", blank=True, null=True)
    sign = models.TextField(default="sign", null=True, blank=True)
    diagnosis = models.CharField(max_length=150, null=True, blank=True)
    intervention = models.CharField(max_length=150, null=True, blank=True)
    amount = models.IntegerField(default= 0)

    def __str__(self):
        return "{}".format(self.id)

    def get_url(self):
        return "/clinic/create/visit/patient/{}/".format(self.patient)
        # return reverse('clinic:pass_patient_id',
        #                 kwargs={'patient': self.patient})

    def get_visit_url(self):
        return reverse('visits:visits_patient_id',
                        kwargs={'id':self.id, 'patient':self.patient})

