from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from datetime import date
from string import ascii_uppercase, digits
import random, os
from apps.visits.models import Visits
from apps.patientdata.models import Patients

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from django.contrib.postgres.search import SearchVector
#

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename)


def validate_none(value):
    if value == None:
        raise ValidationError(_('%(value)s must be not NONE'),
            params={'value': '0'},
        )

# Sample of an ID generator - could be any string/number generator
# For a 6-char field, this one yields 2.1 billion unique IDs
def id_generator(size=6, chars=ascii_uppercase + digits):
    return ''.join(random.choice(chars) for _ in range(size))


def patient_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>_<username>/<filename>
    name = (instance.patient.name).split()
    patient_name = '-'.join(name)
    return 'patient_{0}_{1}/{2}'.format(instance.patient.id, patient_name, filename)


class LabVisit(models.Model):
    name    = models.CharField(max_length=100,
                                help_text="Add analysis Here Please ....")
    result  = models.CharField(max_length=150, null=True, blank=True)
    resdate = models.DateField(default=now)
    image   = models.ImageField(upload_to=patient_directory_path, null=True, blank=True)
    file    = models.FileField(upload_to=patient_directory_path, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    visit   = models.ForeignKey(Visits, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.name)

    def edit_labvisit_url(self):
        # kwargs={'patient_id':self.patient, 'visit':self.visit})
        return reverse('labs:edit_visit_lab', args=(self.patient, self.visit, self.id))


class LabFollowup(models.Model):
    name     = models.CharField(max_length=100,
                                help_text="Add analysis Here Please ....")
    result   = models.CharField(max_length=150, null=True, blank=True)
    resdate  = models.DateField(default=now)
    image    = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    updated  = models.DateTimeField(auto_now=True)
    patient  = models.ForeignKey(Patients, on_delete=models.CASCADE)
    followup = models.ForeignKey(Visits, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.name)

    def edit_followup_url(self):
        # kwargs={'patient_id':self.patient, 'visit':self.visit})
        return reverse('visitdrug:save_medicine', args=(self.patient, self.visit))

