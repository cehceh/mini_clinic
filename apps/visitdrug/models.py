from django.db import models
from django.urls import reverse
from django.utils.timezone import timezone
from datetime import date
from string import ascii_uppercase, digits
import random
from apps.visits.models import Visits
from apps.patientdata.models import Patients

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


class Medicine(models.Model):
    name    = models.CharField(max_length=100,
                            null=True, blank=True, help_text="Add Drug Here Please ....")
    plan    = models.CharField(max_length=150, null=True, blank=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    visit   = models.ForeignKey(Visits, null=True, blank=True, on_delete=models.CASCADE)
    # presc   = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        # return reverse('clinic:save_medicine',
        #                 kwargs={'patient_id':self.patient, 'visit':self.visit})
        return reverse('visitdrug:save_medicine', args=(self.patient, self.visit))
