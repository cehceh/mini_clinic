from django.contrib import admin
from apps.patientdata.models import Patients, Operations

admin.site.register(Patients)
admin.site.register(Operations)

# Register your models here.
# 
class PatientsAdmin(admin.ModelAdmin):
    pass 

