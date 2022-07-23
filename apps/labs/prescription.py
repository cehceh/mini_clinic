from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

# from django.views.generic import View
# from django.template.loader import get_template
# from clinic.utils import render_to_pdf # Justin code
# import time
from django.contrib import messages

from .models import LabVisit
# from .forms import LabVisitForm, LabFollowupForm
from .tables import LabVisitTable

# from apps.patientdata.forms import PatientsForm
from apps.patientdata.models import Patients
# from apps.visits.forms import VisitsForm
from apps.visits.models import Visits


# This method to print prescription
def print_html(request, visit_id):
    visit = Visits.objects.get(id=visit_id)
    table = LabVisitTable(LabVisit.objects.filter(visit=visit_id).order_by('-id'), show_header=False)
    qs = LabVisit.objects.filter(visit=visit_id).order_by('-id') 

    patname = LabVisit.objects.values('patient').filter(visit=visit_id).first()
    patid = LabVisit.objects.values('patient_id').filter(visit=visit_id).first()
    # pat_id = patid['patient_id']
    print(patid)
    match = LabVisit.objects.filter(visit=visit_id).exists()
    if match:
        patient = Patients.objects.get(id=patname['patient'])#patname['patient']
    else:
        patient = None
        messages.success(request, 'Prescription is not ready create new one')
    
    vdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    visitdate = vdate['visitdate']

    context = {
        'match_patient': match,
        'raw_table': table,
        'qs': qs,
        'visit': visit,
        'name': patient,
        'date': visitdate,
        # 'var': 'بسم الله الرحمن الرحيم'
    }
    return render(request, 'labs/print.html', context)

