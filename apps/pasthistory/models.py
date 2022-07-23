from django.db import models
from datetime import date
from apps.patientdata.models import Patients
# Create your models here.

class PastHistory(models.Model):
    pasthist = models.CharField(max_length=150, null=True, blank=True)
    histdate = models.DateField(default=date.today, blank=True, null=True)
    remarknote = models.CharField(max_length=250, blank=True, null=True)
    patient = models.ForeignKey(Patients, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id)


# class DrugHistory(models.Model):
#     drug = models.CharField(max_length=150, null=True, blank=True)
#     patient = models.ForeignKey(Patients,
#                                 null=True,
#                                 blank=True,
#                                 on_delete=models.CASCADE)
#     visit = models.ForeignKey(Visits,
#                             null=True,
#                             blank=True,
#                             on_delete=models.CASCADE)
#     def __str__(self):
#         return "{}".format(self.id)

# class Drugs(models.Model):
#     drug = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return "{}".format(self.drug)


# class Plans(models.Model):
#     plan = models.CharField(max_length=100, null=True, blank=True)

#     def __str__(self):
#         return "{}".format(self.plan)
