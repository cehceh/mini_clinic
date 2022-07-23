from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Max
from django.db import connection, transaction
from django.contrib import messages
# from django.contrib.postgres.search import SearchVector
from apps.patientdata.forms import PatientsForm
from apps.visits.forms import VisitsForm
from .forms import PresentHistoryForm
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.visitdrug.models import Medicine
from .models import PresentHistory
from apps.patientdata.tables import PatientsTable
from apps.visits.tables import VisitsTable
from .tables import PresentHistoryTable



def save_present_hist(request, patient_id, visit_id):
    visit = Visits.objects.get(id=visit_id)
    visitdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    vis_date = visitdate['visitdate']
    visitid = Visits.objects.values('id').filter(id=visit_id).first()
    vis_id = visitid['id']
    patient_name = Patients.objects.get(id=patient_id)
    patientid = Visits.objects.values('patient_id').filter(patient=patient_id).first()
    pat_id = patientid['patient_id']

    match_present = PresentHistory.objects.filter(patient=patient_id).exists()

    qs = PresentHistory.objects.filter(patient=patient_id).order_by('-id')
    table = PresentHistoryTable(qs, exclude="patient, diagnosis, cardid", show_footer=True)
    table.paginate(page=request.GET.get('page', 1), per_page=10)

    match_visit = Medicine.objects.filter(visit=vis_id, patient=pat_id).exists()

    bound_form = PresentHistoryForm(
                                data={
                                        'visitdate':vis_date,
                                        'visit':vis_id,
                                        'patient':patient_name,
                                    })
    if request.method == 'POST':
        form = PresentHistoryForm(request.POST or None)
        if form.is_valid():
            present_form= form.save()
            present_form.visitdate = vis_date
            present_form.patient_id = pat_id
            present_form.visit_id = vis_id
            present_form.save()
            return redirect(
                reverse('presenthistory:edit_present_hist',
                        args=(
                            patient_id,
                            visit_id,
                            present_form.id,                            
                    )))
    else:
        form = PresentHistoryForm()
    context = {
        'save_present_history_form': form,
        'visitform': bound_form,
        'patient': patient_name,
        'visit': visit,
        'match_presen': match_present,
        'medicine': match_visit,
        'all_presenthistory_table': table,
    }
    return render(request, 'presenthistory/add_presenthistory.html', context)


def edit_present_hist(request, patient_id, visit_id, id):
    present = PresentHistory.objects.get(id=id)
    visit = Visits.objects.get(id=visit_id)
    visitdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    vis_date = visitdate['visitdate']
    visitid = Visits.objects.values('id').filter(id=visit_id).first()
    vis_id = visitid['id']
    patient_name = Patients.objects.get(id=patient_id)
    patientid = Visits.objects.values('patient_id').filter(patient=patient_id).first()
    pat_id = patientid['patient_id']

    match_medicine = Medicine.objects.filter(visit=visit_id, patient=patient_id).exists()

    qs = PresentHistory.objects.filter(patient=patient_id).order_by('-id')
    table = PresentHistoryTable(qs, exclude="patient, diagnosis, cardid", show_footer=True)
    table.paginate(page=request.GET.get('page', 1), per_page=10)

    bound_form = PresentHistoryForm(data={
                                        'visitdate':vis_date,
                                        'visit':vis_id,
                                        'patient':patient_name,})

    form = PresentHistoryForm(request.POST or None, instance=present)
    if form.is_valid():
        present_form= form.save()
        present_form.visitdate = vis_date
        present_form.patient_id = pat_id
        present_form.visit_id = vis_id
        present_form.save()
        return redirect(
                reverse('presenthistory:edit_present_hist',
                        args=(
                            patient_id,
                            visit_id,
                            present_form.id,                            
                    )))
        
    context= {
            'edit_present_hist_form': form,
            'match_medicine': match_medicine,
            'present': present,
            'visitform': bound_form,
            'patient': patient_name,
            'visit': visit,
            'all_presenthistory_table': table,
    }
    return render(request, 'presenthistory/edit_presenthistory.html', context)


def patient_history_table(request, patient_id):
    ''' table for specific patient already exists in PresentHistory '''
    visit =  Visits.objects.filter(patient=patient_id).order_by('-id')
    qs = PresentHistory.objects.filter(patient=patient_id).order_by('-id')
    # vis_id = Visits.objects.values('id').filter(patient=patient_id).first()
    # visit_id = vis_id['id']
    
    # patient = Patients.objects.get(id=patient_id)
    # for obj in qs:
    #     obj.
    match_pat = PresentHistory.objects.filter(patient=patient_id).exists()
    # match_pat = PresentHistory.objects.filter(visit=visit_id).exists()
    # print('qs: ' + str(qs) +' vis_id : ' + str(vis_id) + ' vis: ' + str(vis))

    # match_present = PresentHistory.objects.filter(visit=visit_id).exists()
    # if match_pat:
    prehistable = PresentHistoryTable(qs, show_footer=True)
    prehistable.paginate(page=request.GET.get("page", 1), per_page=10)
    # else:
    vistable = VisitsTable(visit,  exclude='edit', show_footer=False)
    vistable.paginate(page=request.GET.get("page", 1), per_page=10)

    context = {
        'table_presenthistory_table': prehistable,
        'vistable_presenthistory_table': vistable,
        'match_pat': match_pat,
    }
    return render(request, 'presenthistory/tables.html', context)


def visit_history_table(request, visit_id):
    qs = PresentHistory.objects.filter(visit=visit_id).order_by('-visitdate')
    visit =  Visits.objects.filter(id=visit_id).order_by('-id')
    match_visit = PresentHistory.objects.filter(visit=visit_id).exists()
    
    if match_visit:
        table = PresentHistoryTable(qs, show_footer=True)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = VisitsTable(visit, show_footer=False)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'table_presenthistory_visit': table,
    }
    return render(request, 'presenthistory/tables.html', context)


def table_add_present_hist(request):
    inner_qs = PresentHistory.objects.all()
    results = Visits.objects.exclude(presenthistory__id__in=inner_qs).order_by('-id')
    # print(results)
    # import os, re, uuid 
    # # joins elements of getnode() after each 2 digits. 
    # # using regex expression 
    # label = os.environ.get('SERIAL')
    # mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    # if mac == label:
    #     messages.success(request, 'you are authorized')
    # else:
    #     messages.success(request, 'you are not authorized')

    page_no = request.GET.get('pageno')
    if page_no == '':
        table = VisitsTable(results, exclude='addrevis')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif page_no == None or int(page_no) == 0:
        page_no = 5
        table = VisitsTable(results, exclude='addrevis')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    else:
        table = VisitsTable(results, exclude='addrevis')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)

    context = {
        'add_present_hist_table':table,
        # 'label': label,
        # 'mac': mac,
    }
    return render(request, 'presenthistory/tables.html', context)


def table_present_hist(request):
    # qs = PresentHistory.objects.select_related('visit')
    qs = PresentHistory.objects.all().order_by('-id')
    # results = Visits.objects.filter(presenthistory__id__in=inner_qs).distinct().order_by('-id')
    # print(qs)

    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = PresentHistoryTable(qs)
        # table = VisitsTable(results, exclude='addrevis, addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = PresentHistoryTable(qs)
        # table = VisitsTable(results, exclude='addrevis, addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    
    context = {
        'present_hist_table':table,
    }
    return render(request, 'presenthistory/tables.html', context)


def delete_history(request, id):
    patient = PresentHistory.objects.values('patient').filter(id=id).first()
    patient_id = patient['patient']
    visit = PresentHistory.objects.values('visit').filter(id=id).first()
    visit_id = visit['visit']
    del_hist = PresentHistory.objects.get(id=id)
    del_hist.delete()

    return redirect(reverse('presenthistory:save_present_hist', args=(patient_id, visit_id)))
    # return redirect(reverse('presenthistory:table_present_hist'))



# get mac address
# def compare(request):
#     '''  '''
#     import re, uuid 

#     # joins elements of getnode() after each 2 digits. 
#     # using regex expression 
#     label = "The MAC address in formatted and less complex way is : "
#     print (label, end="") 
#     mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
#     print (mac) 

#     context = {
#         'label': label,
#         'mac': mac,
#     }
#     return render(request, 'presenthistory/mac.html', context)


