from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Max
from django.db import connection, transaction
from django.contrib import messages

from .forms import PastHistoryForm
from .models import PastHistory
from apps.patientdata.models import Patients
from apps.patientdata.tables import PatientsTable
from apps.visits.tables import VisitsTable
from apps.pasthistory.tables import PastHistoryTable
from apps.presenthistory.tables import PresentHistoryTable

#
def save_pasthist(request, patient_id):

    patient = Patients.objects.get(id=patient_id)
    patientid = Patients.objects.values('id').filter(id=patient_id).first()
    pat_id = patientid['id']

    query = PastHistory.objects.filter(patient=patient_id).order_by('-histdate')
    table = PastHistoryTable(query, exclude='add, patient')
    
    bound_form = PastHistoryForm(data={'patient':patient})#(instance=patient)
    if request.method == 'POST':
        form = PastHistoryForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.patient_id = patient_id
            save_form.save()
            messages.success(request, 'Saving history done')
            return redirect(reverse('pasthistory:save_pasthist', kwargs={'patient_id': patient_id}))
    else:
        form = PastHistoryForm()
       
    context = {
        'patient': patient,
        'boundform': bound_form,
        'save_pasthist_form': form,
        'pasthist_table': table,
    }
    return render(request, 'pasthistory/add_pasthistory.html', context)


def edit_pasthist(request, patient_id, id):
    patient = Patients.objects.get(id=patient_id)
    patientid = Patients.objects.values('id').filter(id=patient_id).first()
    pat_id = patientid['id']

    query = PastHistory.objects.filter(patient=patient_id).order_by('-histdate')
    table = PastHistoryTable(query, exclude='add, patient')
    table.paginate(page=request.GET.get('page', 1),per_page=10)
    
    pasthist = PastHistory.objects.get(id=id)
    
    form = PastHistoryForm(request.POST or None, instance=pasthist)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.patient_id = patient_id
        save_form.save()
        messages.success(request, 'Save changes done')
        return redirect(reverse('pasthistory:edit_pasthist', kwargs={'patient_id': pat_id, 'id': id}))
    # else:
    #     form = PastHistoryForm()
    context = {
        'patient': patient,
        # 'query': query,
        # 'boundform': bound_form,
        'edit_pasthist_form': form,
        'pasthist_table':table,
    }
    return render(request, 'pasthistory/edit_pasthistory.html', context)


def pasthist_table(request): # all past history record
    var = Patients.objects.all()
    # var = PastHistory.objects.values('patient', 'histdate', 'pasthist').distinct()
    # var = PastHistory.objects.select_related('patient').distinct().order_by('-id')
    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = PatientsTable(var, exclude='addr, age, birth, tele, mob')
        table.paginate(page=request.GET.get("page", 1), per_page=25)
    else:
        table = PatientsTable(var, exclude='addr, age, birth, tele, mob')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    
    context = {
        'pasthist_table':table,
    }
    return render(request, 'patientdata/tables.html', context)


def delete_pasthist(request, id):
    query = PastHistory.objects.get(id=id)

    pat = PastHistory.objects.values('patient_id').filter(id=id).first()
    patid = pat['patient_id']
    query.delete()

    return redirect(reverse('pasthistory:save_pasthist', kwargs={'patient_id': patid}))


