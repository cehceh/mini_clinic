from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Medicine
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.pasthistory.models import PastHistory
from apps.presenthistory.models import PresentHistory
from .forms import MedicineForm
from .tables import MedicineTable


def save_medicine(request, patient_id, visit_id):
    ''' Method for saving patient's medicine '''
    # last = Medicine.objects.values('presc').last()
    # if last is None:
    #     last = {'presc':1}
    # else:
    #last = Medicine.objects.values('presc').last()
    page_no = request.GET.get('pages')
    if request.GET.get('pages') == "0":
        page_no = "1"
        
    queryset = Medicine.objects.filter(visit=visit_id).order_by('-id')
    table = MedicineTable(Medicine.objects.filter(visit=visit_id).order_by('-id'), exclude='patient')
    # table = MedicineTable(Medicine.objects.filter(visit=visit_id,
    #                                               patient=patient_id).order_by('-id'),exclude='patient')
    # page_no = request.GET.get('pages')
    table.paginate(page=request.GET.get("page", 1), per_page=page_no)

    patient = Patients.objects.get(id=patient_id) #
    patientid = Visits.objects.values('patient_id').filter(patient_id=patient_id).first()

    qs = Visits.objects.values('patient_id').filter(id=visit_id, patient=patient_id).first()
    # qsvalue = qs['patient']

    visit_func = Visits.objects.get(id=visit_id) #
    # print('visit_func: ' + str(visit_func))
    visitid = Visits.objects.values('id').filter(id=visit_id).first()
    visdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    pat_name = Visits.objects.values('patient').filter(id=visit_id).first()
    name = pat_name['patient']
    # print(patientid, visitid, qs)

    pat_id = patientid['patient_id']
    vis_id = visitid['id']
    vis_date = visdate['visitdate']
    bound_form = MedicineForm(data={'visit':vis_id, 'patient':patient,})
    # visit_form_pat = MedicineForm(data={'patient':patient})
    # print(vis_id, pat_id)
    v = request.POST.get('visit')#request.POST.get('visit')
    p = request.POST.get('patient')
    match_visit = Medicine.objects.filter(visit=vis_id,
                                        patient=pat_id).exists()
    # print(match_visit)
    #Check if this visit No. is in the PresentHistory table or not
    match_present = PresentHistory.objects.filter(visit=vis_id).exists()
    
    # print('after check visit= ' + str(visit), str(v), str(p))
    if request.method == 'POST':# and form.is_valid():
        form = MedicineForm(request.POST or None)
        # print('form POST')
        if form.is_valid():
            pat = request.POST.get('patient') #request.POST.get('patient')
            vis = request.POST.get('visit')
            match = Visits.objects.filter(id=vis, patient=pat).exists()
            # if match: 
            match_row = len(table.rows)
                # print(match_row)
            if match_row < 8:
                save_form = form.save(commit=False)
                save_form.patient_id = patient_id
                save_form.visit_id = visit_id
                save_form.save()
                bound_form = MedicineForm(data={'visit':vis_id, 'patient':patient,})
            
                return HttpResponseRedirect(
                    reverse('visitdrug:save_medicine',
                            args=(pat_id, vis_id)))  # that's it()
            else:
                messages.success(request, 'You can\'t add more than 8 drugs per one prescription, \nFor any inquiries contact Eng. Amr Ammer on 01067174141')
            # else:
            #     messages.success(
            #         request, 'Visit No. must be ' + str(vis_id) +
            #         ', and Patient name must be ' + str(patient))
    else:
        form = MedicineForm()
       
    context = {
        'page_no': page_no,
        'present': match_present,
        'match_visit': match_visit,
        'queryset': queryset,
        'drug_table': table,
        'vis_date': vis_date,
        'patient': patient,
        'visit': visit_func,
        'patid': pat_id,
        'visid': vis_id,
        'visit_form': bound_form,
        'save_medicine_form': form,
    }
    return render(request, 'visitdrug/add_visitdrug.html', context)


def edit_medicine(request, patient_id, visit_id, id):  # Making Update to a Medicine
    table = MedicineTable(Medicine.objects.filter(visit=visit_id).order_by('-id'), exclude='patient')
    # page_no = request.GET.get('pages')
    table.paginate(page=request.GET.get("page", 1), per_page=10)

    patient = Patients.objects.get(id=patient_id) #
    patientid = Visits.objects.values('patient_id').filter(patient_id=patient_id).first()
    # name = patientid['patient_id'] # this error 'NoneType' object is not subscriptable (occurs when i put another parameter in filter)

    visit = Visits.objects.get(id=visit_id) # out put is the visit ID
    visitid = Visits.objects.values('id').filter(id=visit_id).first() # out put is {'id':its value}
    visdate = Visits.objects.values('visitdate').filter(id=visit_id).first() # out put is {'visitdate':its value}

    # pat_name = Patients.objects.get(id=name) # out put is {'visitdate':its value}
    # print(patientid, visitid)
    pat_id = patientid['patient_id']
    vis_id = visitid['id']
    vis_date = visdate['visitdate']
    name = Visits.objects.filter(patient=pat_id)

    first_rec = Medicine.objects.values('patient').filter(visit=vis_id, patient=pat_id).first()
    # name = first_rec['patient']

    drug = Medicine.objects.values('id').filter(id=id).first()
    drug_id = drug['id']
    # return True or False
    match = Medicine.objects.filter(visit=vis_id, patient=pat_id).exists()
    # print(str(patientid)+ ', ' + 'match in medicine= ' + str(match) + ' , ' + str(vis_id) + ' , ' + str(name))

    query = Medicine.objects.get(id=id)  # The output is the medicine ID
    form = MedicineForm(request.POST or None, instance=query)
    if form.is_valid():
        # vis = request.POST.get('visit')
        # pat = request.POST.get('patient')
        # match = Visits.objects.filter(id=vis, patient=pat).exists()
        # if match:
        save_form = form.save(commit=False)
        save_form.patient_id = patient_id
        save_form.visit_id = visit_id
        save_form.save()
        return redirect(reverse('visitdrug:save_medicine', args=(pat_id, vis_id)))
        #  HTTPResponseRedirect(reverse('patientdata:edit_patient', kwargs={'id': id}))
        # else:
        #     messages.success(request, 'Visit No must be ' + str(vis_id) + ', And patient name must be ' + str(patient))
    context = {
        'drug': query,
        'patient': patient,
        'visit': visit,
        'visid': vis_id,
        'patid': pat_id,
        'vis_date': vis_date,
        'drug_table': table,
        'edit_medicine_form': form
    }
    return render(request, 'visitdrug/edit_visitdrug.html', context)


def table_medicine(request):
    table = MedicineTable(Medicine.objects.all().order_by('-id'))
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    context = {
        'table_medicine': table
    }
    return render(request, 'tables.html', context)
# HttpResponse for http direct write

def delete_medicine(request, patient, visit, id):
    pat_id = Patients.objects.get(id=patient)
    vis_id = Visits.objects.get(id=visit)

    pat = Medicine.objects.values('patient_id').filter(patient_id=pat_id).first()
    patient_id = pat['patient_id']
    vis =  Medicine.objects.values('visit').filter(visit=visit).first()
    visit_id = vis['visit']

    qs = Medicine.objects.get(id=id)
    del_med = qs.delete()

    print(pat, patient_id)
    return redirect(reverse('visitdrug:save_medicine', args=(patient_id, visit_id)))


def add_new(request, patient_id, visit_id):
    ''' Method for saving patient's medicine '''
    # last = Medicine.objects.values('presc').last()
    # # print('last = ' + str(last))
    # if last is None:
    #     last = {'presc':1}
    # else:
    #     last = Medicine.objects.values('presc').last()

    # match_last = Medicine.objects.filter(visit=visit_id, patient=patient_id, presc=last['presc']).exists()
    # if match_last:
    #     presc = last['presc'] + 1
    # else:
    #     presc = last['presc']

    queryset = Medicine.objects.filter(visit=visit_id).order_by('-id')
    # q = Medicine.objects.filter(visit=visit_id, patient=patient_id, presc=last['presc'])
    # print('q = ' + str(q))
    table = MedicineTable(Medicine.objects.filter(
        visit=visit_id, patient=patient_id).order_by('-id'),
                          exclude='patient')
    # table = MedicineTable(
    #     Medicine.objects.select_related('visit', 'patient').order_by('-id'))
    # print(Medicine.objects.select_related('visit', 'patient').order_by('-id').query)
    # page_no = request.GET.get('pages')
    table.paginate(page=request.GET.get("page", 1), per_page=3)

    patient = Patients.objects.get(id=patient_id) #
    patientid = Visits.objects.values('patient_id').filter(patient_id=patient_id).first()

    qs = Visits.objects.values('patient_id').filter(id=visit_id, patient=patient_id).first()
    # qsvalue = qs['patient']

    visit_func = Visits.objects.get(id=visit_id) #
    print('visit_func: ' + str(visit_func))
    visitid = Visits.objects.values('id').filter(id=visit_id).first()
    visdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    pat_name = Visits.objects.values('patient').filter(id=visit_id).first()
    name = pat_name['patient']
    print(patientid, visitid, qs)

    pat_id = patientid['patient_id']
    vis_id = visitid['id']
    vis_date = visdate['visitdate']
    bound_form = MedicineForm(data={'visit':vis_id, 'patient':patient,})
    # visit_form_pat = MedicineForm(data={'patient':patient})
    print(vis_id, pat_id)
    v = request.POST.get('visit')#request.POST.get('visit')
    p = request.POST.get('patient')
    match_visit = Medicine.objects.filter(visit=vis_id,
                                          patient=pat_id).exists()

    print(match_visit)

    if request.method == 'POST':# and form.is_valid():
        form = MedicineForm(request.POST or None)
        print('form POST')
        if form.is_valid():
            pat = request.POST.get('patient') #request.POST.get('patient')
            vis = request.POST.get('visit')
            match = Visits.objects.filter(id=vis, patient=pat).exists()
            # match = Medicine.objects.filter(visit=vis, patient=pat).exists()
            # print(str(pat) + ' - ' + str(vis) + ' - ' + str(match))
            print(pat,vis,match)
            if match: #match_row < 2:#(vis == vis_id) and (pat == pat_id)
                match_row = len(table.rows)
                print(match_row)
                if match_row < 3:
                    form.save()
                    # bound_form = MedicineForm(
                    #     data={
                    #         'visit': vis_id,
                    #         'patient': patient,
                    #         'presc': (last['presc'] - 1)
                    #     })
                    # instance = form.save()
                    # instance.save()
                    # print('what is going on here2')
                    return HttpResponseRedirect(
                        reverse('visitdrug:add_new',
                                args=(pat_id, vis_id)))  # that's it()
                else:
                    messages.success(request, 'Drugs reach to its limit, You are in a demo mode')
            else:
                messages.success(
                    request, 'Visit No. must be ' + str(vis_id) +
                    ', and Patient name must be ' + str(patient))
    else:
        form = MedicineForm()
        # bound_form = MedicineForm(data={'visit':vis_id, 'patient':patient, 'presc':(last['presc']+1)})
    context = {
        'match_visit': match_visit,
        'queryset': queryset,
        'drug_table': table,
        'vis_date': vis_date,
        'patient': patient,
        'visit': visit_func,
        'patid': pat_id,
        'visid': vis_id,
        'visit_form': bound_form,
        'save_medicine_form': form,
    }
    return render(request, 'visitdrug/clinic.html', context)


