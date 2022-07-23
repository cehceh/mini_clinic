from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Max
from django.db import connection, transaction
from django.contrib import messages
# from django.contrib.postgres.search import SearchVector

from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.visitdrug.models import Medicine
from apps.revisitdrug.models import Remedicine 
from apps.presenthistory.models import PresentHistory
from apps.patientdata.tables import PatientsTable
from apps.visits.tables import VisitsTable

from .models import Revisits
from .forms import RevisitsForm
from .tables import RevisitsTable


# new save revisit 
def save_revisit(request, patient_id, visit_id): # Making save to new visits
    patient = Patients.objects.get(id=patient_id) # out put is the patient name
    patid = Patients.objects.values('id').filter(id=patient_id).first() # This is out put of without .first()=> <QuerySet [{'id': 36}]>
    var = patid['id']
    
    visit = Visits.objects.get(id=visit_id)
    # visitdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    # vis_date = visitdate['visitdate']
    visitid = Visits.objects.values('id').filter(id=visit_id).first()
    vis_id = visitid['id']

    match_present = PresentHistory.objects.filter(visit=visit_id).exists()
    present = PresentHistory.objects.values('id').filter(visit=visit_id).first()
    if not match_present:
        present = None #PresentHistory.objects.all()
        present_qs = None
    else:
        presentid = present['id']
        present_qs = PresentHistory.objects.get(id=presentid)

    match_medicine = Medicine.objects.filter(visit=visit_id).exists()
    match_revisit_medicine = Remedicine.objects.filter(visit=visit_id).exists()
    # if match_medicine:
    #     medicine = Medicine.objects.get(visit=visit_id)
    # else:
    #     medicine = None
    
    bound_form = RevisitsForm(data={
                'patient':patient, 
                'visit':visit,
                # 'visitdate':vis_date,
                })
    
    if request.method == 'POST':
        form = RevisitsForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.patient_id = patient_id
            save_form.visit_id = visit_id
            save_form.save()
            return redirect(reverse('revisits:view_revisit',  args=(visit_id, patient_id)))#kwargs={'visit':visit_id, 'patient':patient_id}))
    else:
        form = RevisitsForm()
    
    context = {
        'visit': visit,
        'present': match_present,
        'present_id': present_qs,
        'pat_id': var,
        'patient': patient, 
        'medicine': match_medicine,
        'remidicine': match_revisit_medicine,
        'save_revisits_form': form,
        'bound_form': bound_form,
    }
    return render(request, 'revisits/add_revisit.html', context)

#
def edit_revisit(request, patient_id, visit_id, id):
    query = Revisits.objects.get(id=id)  # out put Revisit ID
    qs = Revisits.objects.values('patient_id').filter(patient_id=patient_id).first() # {'patient_id': 2}
    # for get_url() to redirect to -save present history- form
    # test = Visits.objects.values('id', 'patient')\
    #                     .filter(id=id, patient=patient_id).first()  # {'id': 136, 'patient': 15}
    # print(qs, test)
    visit = Visits.objects.get(id=visit_id) # 
    
    patient = Patients.objects.get(id=patient_id) # Use it with get_absolute_url()
    patientid = qs['patient_id'] # out put is Patient ID
    
    match_present = PresentHistory.objects.filter(visit=visit_id).exists()
    if not match_present:
        present = None #PresentHistory.objects.all()
    else:
        present = PresentHistory.objects.get(visit=visit_id)

    bound_form = RevisitsForm(data={
                                    'patient':patient, 
                                    'visit':visit,
                                    # 'visitdate':vis_date,
                                    })

    form = RevisitsForm(request.POST or None, instance=query)
    if form.is_valid():
        # patid = request.POST.get('patient')
        # # print('patid : ' + str(patid))
        # match = Visits.objects.filter(patient_id=patid, id=visit_id).exists()
        # if match:
        save_form = form.save(commit=False)
        save_form.patient_id = patient_id
        save_form.visit_id = visit_id
        save_form.save()
        # print(patid)
        return redirect(reverse('revisits:edit_revisit', args=(query, patientid, visit_id)))  # ('/clinic/table/')
        #  HTTPResponseRedirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
        # else:
        #     messages.success(request, 'The Patient Name Must Be : ' + \
        #     str(patient) + ', With Patient ID : ' + str(patient_id) + ' Not Ptient ID : ' + str(patid))

    context = {
        'patient': patient,
        'patient_id': patientid,
        'query': query,
        'present': match_present,
        'present_id': present,
        'visit': visit,
        'bound_form': bound_form,
        'edit_revisits_form': form,
    }
    return render(request, 'revisits/edit_revisit.html', context)

#
def table_revisit(request):
    qs = Revisits.objects.select_related('patient', 'visit')#.order_by('id')
    # ('-visits_visits.id') # the next lines are the result of this query ORM
    # qs = Revisits.objects.all().order_by('-id')
    print(qs.query)
    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = RevisitsTable(qs, exclude='prn')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = RevisitsTable(qs, exclude='prn')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)

    # print(qs.query)
    context = {
        # 'qs_table': qs,
        'revisits_table': table,
    }
    return render(request, 'revisits/tables.html', context)

def view_revisit(request, visit_id, patient_id):
    visit = Visits.objects.get(id=visit_id)
    patient = Patients.objects.get(id= patient_id)
    qs = Revisits.objects.filter(visit=visit_id).order_by('-id')
    table = RevisitsTable(qs, exclude='patient, visit')
    table.paginate(page=request.GET.get("page", 1), per_page=10)

    context = {
        'visit': visit,
        'patient': patient,
        'view_revisits_table': table,
    }
    return render(request, 'revisits/tables.html', context)

def delete_revisit(request, id):
    del_revisit = Revisits.objects.get(id=id)
    del_revisit.delete()
    return redirect('revisits:table_revisit')



# def table_revisit(request):
#     # qs = Revisits.objects.select_related('patient').order_by('-id') # the next lines are the result of this query ORM
#     # qs = Visits.objects.all().order_by('-id')
#     qs = Revisits.objects.all().order_by('-id')
#     table = RevisitsTable(qs, exclude='addpresent')
#     table.paginate(page=request.GET.get("page", 1), per_page=10)
#     print(qs.query)
#     context = {
#         # 'qs_table': qs,
#         'revisits_table': table,
#     }
#     return render(request, 'revisitdata/tables.html', context)
