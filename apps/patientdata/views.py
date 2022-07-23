from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q, Sum, Max, Count
from django.db import connection, transaction
from django.contrib import messages
from datetime import date
# from django.db.models.expressions import RawSQL

# from django.db.models import Q
import os, re, uuid
from django.core.exceptions import PermissionDenied

from .forms import PatientsForm
from .models import Patients
from .tables import PatientsTable
# from apps.revisits.prescriptions import auth_required
from apps.pasthistory.models import PastHistory
from apps.presenthistory.models import PresentHistory
from apps.visits.models import Visits
from apps.visits.tables import VisitsTable

import sysconfig
sysconfig.get_paths()['stdlib'] + 'mypackage'
from mypackage.myfile import * 
# print(sysconfig.get_paths()['stdlib'] + 'mypackage')
# 

@auth_required
def save_patient(request):
    print(sysconfig.get_paths()['stdlib'] + '\mypackage')    
    """ Collecting data for patients function to save patient data to database """ 
    # dup_name = Patients.objects\
    #                 .values('birth_date')\
    #                 .annotate(ncount=Count('birth_date'))\
    #                 .filter(birth_date='1989-04-25')
    # count = Patients.objects.filter(name='Ahmed').count()
    # print(str(count), 'dupName= '+str(dup_name[0]['ncount']))
    if request.method == 'POST':
        form = PatientsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data['name'] #request.POST.get('name')
            print(name)
            match = Patients.objects.filter(name=name).exists()
            if not match:
            #     qr.png('media_root/patients/' + str(img_name) + '.png', scale=8)
                save_form = form.save(commit=False)
                # save_form.barimg = 'patients/' + str(img_name) + '.png' 
                # save_form.barurl = barcode_value
                save_form.save()
                pat_id = save_form.id
                Visits.objects.create(patient_id=pat_id, visitdate=date.today(),
                                complain="any comp", sign="any sign", 
                                amount=0, intervention="any intervention")
                messages.success(request, 'Saving process done ... ')
                return redirect('patientdata:table_patient')
            else:
                messages.error(request, 'Patient name already exsits')
                return redirect(reverse('patientdata:save_patient'))
    else:
        form = PatientsForm()

    lastid = Patients.objects.values('id').last()
    if lastid is not None:
        patid = lastid['id'] + 1
    else:
        patid = 1
    # print(patid)
    label2 = "Save"
    context = {
        'savepatform': form,
        'lastid': patid,
        # 'button_lable': label,
        'lable2': label2,
    }
    return render(request, 'patientdata/save_patient.html', context)


@auth_required 
def edit_patient(request, id): # Making Update to a Patient
    qs = Visits.objects.filter(patient=id).order_by('-id')
    # print('qs = '+str(qs))
    # match_presenthist = PresentHistory.objects.filter(patient=id, visit=1).exists()
    table = VisitsTable(qs, exclude='patient, addpresent')
    table.paginate(page=request.GET.get("page", 1), per_page=10)

    query = Patients.objects.get(id=id)  
    patient = Patients.objects.values('id').filter(id=id).first()
    barcode = Patients.objects.values('barcode').filter(id=id).first()
    # patient = Patients.objects.filter(id=id)
    patient_id = patient['id']
    bar = barcode['barcode']
    print('query.name(before):', query.name)
    match_pasthist = PastHistory.objects.filter(patient=id).exists()
    # if match_pasthist:
    #     pasthist = PastHistory.objects.values('id').filter(patient=patient_id).first()
    
    form = PatientsForm(request.POST or None, instance=query)
    # print(form)
    if form.is_valid():
        # name = request.POST.get('name')
        # name = form.cleaned_data['name']
        query = Patients.objects.get(id=id) # very important query to get the original name if duplication occurs
        save_form = form.save(commit=False)
        save_form.save()
        patient_id = save_form.id           # very important line to get the original name if duplication occurs
        name = save_form.name  
        match = Patients.objects.filter(name=name).exists()
        print('query.name(after):', query, 'name(after saving):', name)
        dup_name = Patients.objects \
                        .values('name') \
                        .annotate(ncount=Count('name')) \
                        .filter(name=name, ncount__gt=1)
        records = Patients.objects \
                        .filter(name__in=[item['name'] for item in dup_name])
        print(dup_name, records)
        rec = [item.name for item in records]
        reco = any(rec.count(element) > 1 for element in rec)
        print('patname= '+str(name), 'rec_edit= '+str(rec), 'dupname_edit= ' , str(dup_name),reco)
        # if not match:
        if not reco: #or reco_num
            # save_form = form.save(commit=False)
            # save_form.save()
            # patient_name = save_form.name   
            messages.success(request, 'Edit changes done successfully for Patient (' +str(name)+ ')')
            return redirect(reverse('patientdata:edit_patient', kwargs={'id':id}))
            # return redirect(reverse('patientdata:table_patient'))
            # if reco:
        else:
            messages.error(request, 'Patient (' +str(name)+ ') is already exists change the patient name ..!')
            Patients.objects.filter(id=patient_id).update(name=query.name)
            return redirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
        # else:
        #     messages.error(request, 'Patient (' +str(name)+ ') exists  change the name ..!')
        #         # Patients.objects.filter(id=patient_id).update(name=db_name.name)
        #     return redirect(reverse('patientdata:edit_patient', kwargs={'id': id})) 

    context = { 
        'patient': patient,
        'patient_id': patient_id,
        'editpatform': form,
        'query': query,
        'barcode': bar,
        'match_pasthist': match_pasthist,
        'patient_visits_table':table,
    }
    return render(request, 'patientdata/edit_patient.html', context)


@auth_required
def table_patient(request):
    qs = Patients.objects.all().order_by('-id')[:50]

    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = PatientsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif page_no != None or page_no != '' or int(page_no) != 0:
        table = PatientsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    else:
        table = PatientsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=10) 
    
    context = {
        'table_patient': table
    }
    return render(request, 'patientdata/tables.html', context)


# def patient_details(request, barcode):
#     qs = Patients.objects.get(barcode=barcode)
#     patient = Patients.objects.get(id=qs.id)

#     visit_table = VisitsTable(Visits.objects.filter(patient=qs.id), exclude='patient,diagnosis,amount,addpresent,')
#     visit_table.paginate(page=request.GET.get("page", 1), per_page=5)

#     context = {
#         'qs': qs,
#         'patient': patient,
#         'visit_table': visit_table,
#     }
#     return render(request, 'patientdata/patient_details.html', context)


# def barcode_redirect(request, barcode):
#     qs = Patients.objects.get(barcode=barcode)
    
    
#     return redirect(reverse('patientdata:edit_patient', args=(qs.id)))







    # search_name = request.GET.get('patname')
    # search_id = request.GET.get('patid')
    # result = Patients.objects.filter(Q(name__icontains=search_name))
    # result_id = Patients.objects.filter(Q(id=search_id))
    
# if search_name != '':
    #     table = PatientsTable(result)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif search_id != None or search_id != '' or int(search_id) != 0:
    #     table = PatientsTable(result_id)
    # elif search_id == None or search_id == '' or int(search_id) == 0:
    #     table = PatientsTable(qs)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif page_no == None or page_no == '' or int(page_no) == 0:
    #     table = PatientsTable(qs)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)

    # elif search_name == '':
    #     table = PatientsTable(qs)
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif search_name == '' and  page_no == '' and search_id == '':
    #     table = PatientsTable(result)
    #     table.paginate(page=request.GET.get("page", 1), per_page=2)