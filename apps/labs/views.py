from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from datetime import date

from .forms import LabVisitForm, LabFollowupForm
from .models import LabVisit, LabFollowup
from .tables import LabVisitTable

from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.visits.tables import VisitsTable


import sysconfig
sysconfig.get_paths()['stdlib'] + 'mypackage'
from mypackage.myfile import * 

# Create your views here.

@auth_required
def add_lab_visit(request, patient_id, visit_id, *args, **kwargs):
    '''  '''
    patient = Patients.objects.get(id=patient_id)
    visit = Visits.objects.values('visitdate').filter(id=visit_id).first()
    visdate = visit['visitdate']
    
    # name = kwargs.get('patient')
    # print('name= ', name)
    match_lab = LabVisit.objects.filter(visit=visit_id,
                                        patient=patient_id).exists()

    if request.method == 'POST':
        form = LabVisitForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            lab_form = form.save(commit=False)
            lab_form.visit_id = visit_id
            lab_form.patient_id = patient_id
            lab_form.resdate = date.today()
            lab_form.save()
            messages.success(request, 'Saving analysis done ...')
            return redirect(reverse('labs:add_lab_visit', args=(patient_id, visit_id)))
    else:
        form = LabVisitForm()

    qs = LabVisit.objects.filter(visit=visit_id).order_by('-id')
    table = LabVisitTable(qs, exclude='id, visit, patient, addlab, result, resdate')
    table.paginate(page=request.GET.get("page", 1), per_page=10)

    context = {
        'visit': visit,
        'patient': patient,
        'lab_form': form,
        'patid': patient_id,
        'visid': visit_id,
        'lab_table': table,
        'vis_date': visdate,
        'match_lab': match_lab,
    }

    return render(request, 'labs/add_lab_visit.html', context)


def add_lab_followup(request, patient_id, followup_id):
    '''  '''
    if request.method == 'POST':
        form = LabFollowupForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            lab_form = form.save(commit=False)
            lab_form.followup = followup_id
            lab_form.patient = patient_id

            lab_form.save()
    else:
        form = LabFollowupForm()
    context = {
        'form': form,
    }

    return render(request, 'labs/add_lab_followup.html', context)


def edit_lab_visit(request, lab_id, patient_id, visit_id):
    '''  '''
    visit = Visits.objects.values('visitdate').filter(id=visit_id).first()
    visdate = visit['visitdate']

    match = LabVisit.objects.filter(id=lab_id).exists()
    if match:
        lab = LabVisit.objects.get(id=lab_id)
        form = LabVisitForm(request.POST or None, request.FILES or None, instance=lab)
    else:
        return redirect(reverse('labs:add_lab_visit', args=(patient_id, visit_id)))

    if form.is_valid():
        lab_form = form.save(commit=False)
        lab_form.visit_id = visit_id
        lab_form.patient_id = patient_id
        lab_form.save()
        messages.success(request, 'Saving changes done ...')
        return redirect(reverse('labs:edit_lab_visit', args=(lab_id, patient_id, visit_id)))

    qs = LabVisit.objects.filter(visit=visit_id).order_by('-id')
    table = LabVisitTable(qs, exclude='id, visit, patient, addlab')
    table.paginate(page=request.GET.get("page", 1), per_page=10)

    context = {
        'lab_form': form,
        'patid': patient_id,
        'visid': visit_id,
        'lab_id': lab_id,
        'lab_table': table,
        'lab': lab,
        'vis_date': visdate,        
    }

    return render(request, 'labs/edit_lab_visit.html', context)


def edit_lab_followup(request, lab_id, patient_id, followup_id):
    '''  '''
    qs = LabFollowup.objects.get(id=lab_id)
    form = LabVisitForm(request.POST or None, request.FILES or None, instance=qs)
    context = {

    }

    return render(request, 'labs/edit_lab_followup.html', context)


def lab_visit_table(request):
    '''  '''
    var = Visits.objects.all().order_by('-id')
    # var = PastHistory.objects.values('patient', 'histdate', 'pasthist').distinct()
    # var = PastHistory.objects.select_related('patient').distinct().order_by('-id')
    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = VisitsTable(var, exclude='diagnosis, addpresent, addrevis')
        table.paginate(page=request.GET.get("page", 1), per_page=25)
    else:
        table = VisitsTable(var, exclude='diagnosis, addpresent, addrevis')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    
    context = {
        'lab_visit_table':table,
    }

    return render(request, 'labs/lab_visit_table.html', context)


def lab_followup_table(request):
    '''  '''
    context = {

    }

    return render(request, 'labs/tables.html', context)


def delete_lab_visit(request, lab_id, patient_id, visit_id):
    '''  '''
    lab_visit = LabVisit.objects.get(id=lab_id)
    lab_visit.delete()
    return redirect(reverse('labs:add_lab_visit', args=(patient_id, visit_id)))


def delete_lab_followup(request):
    '''  '''
    return redirect('/')
