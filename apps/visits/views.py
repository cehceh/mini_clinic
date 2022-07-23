from apps.labs.models import LabVisit
from django.shortcuts import render, redirect, reverse
# from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q, Count

from .models import Visits
from apps.patientdata.models import Patients
from apps.presenthistory.models import PresentHistory
from apps.pasthistory.models import PastHistory

# from apps.revisits.models import Revisits
from .forms import VisitsForm
from .tables import VisitsTable
from apps.visitdrug.tables import MedicineTable
from apps.visitdrug.models import Medicine
from django.contrib import messages

from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport


def export_table(request):
    table = VisitsTable(Visits.objects.all())

    RequestConfig(request).configure(table)

    export_format = request.GET.get("csv, json", None)
    if TableExport.is_valid_format(export_format):
        # exclude columns while creating the TableExport instance:
        # exporter = TableExport("csv", table, exclude_columns=("image", "buttons"))
        exporter = TableExport(export_format, table, dataset_kwargs={"title": "My Custom Sheet Name"})
        # exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    return render(request, "tables.html", {
        "export_table": table,
    })


# new save visit
def pass_patient_id(request, id): # Making save to new visits
    patient = Patients.objects.get(id=id) # out put is the patient name
    patient_id = Patients.objects.values('id').filter(id=id).first() # This is out put of without .first()=> <QuerySet [{'id': 36}]>
    var = patient_id['id']
    
    count = Visits.objects.filter(visitdate='2021-04-25').count()
    print(count)
    # var1 = Patients.objects.values('mobile').filter(id=id).first()
    # var11 = var1['mobile']
    # print(patient, patient_id)
    match_pasthist = PastHistory.objects.filter(patient=id).exists()

    bound_form = VisitsForm(data={'patient':patient})
    
    if request.method == 'POST':
        form = VisitsForm(request.POST or None)
        if form.is_valid():
            save_form = form.save(commit=False)
            save_form.patient_id = var
            save_form.save()
            visit_id = save_form.id
            # name = save_form.patient
            messages.success(request, 'Saving new visit for (' + str(patient) + ') done')
            return redirect(reverse('visits:visits_patient_id', args=(visit_id, save_form.patient_id)))#('visits:table_visits')
    else:
        form = VisitsForm()
    context = {
        'pat_id': var,
        'patient': patient,
        'match_pasthist':match_pasthist,
        'save_visits_form': form,
        'bound_form': bound_form,
    }
    return render(request, 'visits/add_visit.html', context)


# new edit visit
def visits_patient_id(request, id, patient_id):  # Making Update to a visit with knowing the patient id
    query = Visits.objects.get(id=id)  # out put Visit ID
    # query = Visits.objects.select_related('patient').get(id=id)  # out put Visit ID
    qs = Visits.objects.values('id', 'patient_id').filter(id=id, patient_id=patient_id).first() # {'patient_id': 2}
    # for get_url() to redirect to -save present history- form
    visid = Visits.objects.values('id')\
                        .filter(id=id).first()  # {'id': 136, 'patient': 15}
    vis_id = visid['id']
    
    match_medicine = Medicine.objects.filter(visit=id).exists()
    # match_medicine = Medicine.objects.select_related('visit').filter(visit=id).exists()
    # print('true or false : ',match_medicine)
    # if match_medicine:
    #     medicine = Medicine.objects.get(visit=id)
    # else:
    #     medicine = None

    match_present = PresentHistory.objects.filter(visit=id).exists()
    # if not match_present:
    #     present = None #PresentHistory.objects.all()
    # else:
    from django.conf import settings
    debug = settings.DEBUG
    
    present = PresentHistory.objects.values('id').filter(visit=id).first()
    if present != None:
        presentid = present['id']
    else:
        presentid = 0
    # print(present, presentid)
    if presentid == 0:
        present_qs = 0
    else:
        present_qs = PresentHistory.objects.get(id=presentid)

    match_lab = LabVisit.objects.filter(visit_id=id).exists()

    patient = Visits.objects.select_related('patient').get(id=patient_id) 
    # patient = Patients.objects.get(id=patient_id) # Use it with get_absolute_url()
    # print('patient: ', patient)
    patientid = qs['patient_id'] # out put is Patient ID
    form = VisitsForm(request.POST or None, instance=query)
    if form.is_valid():
        # patid = request.POST.get('patient')
        # # print('patid : ' + str(patid))
        # match = Visits.objects.filter(patient_id=patid, id=id).exists()
        # if match:
        save_form = form.save(commit=False)
        save_form.patient_id = patient_id
        # save_form.visit_id = id
        save_form.save()
        messages.success(request, 'Update visit no. (' + str(vis_id) + ') done successfully' )
        return redirect(reverse('visits:visits_patient_id', args=(vis_id, patientid)))  # ('/clinic/table/')
        #  HTTPResponseRedirect(reverse('clinic:edit_patient', kwargs={'id': id}))
        # else:
        #     messages.success(request, 'The Patient Name Must Be : ' + \
        #     str(patient) + ', With Patient ID : ' + str(patient_id) + ' Not Ptient ID : ' + str(patid))

    context = {
        # 'debug': debug,
        'patient': patient,
        'patient_id': patientid,
        'visit': query,
        'vis_id': vis_id,
        'qs': qs,
        'medicine': match_medicine,
        # 'medicine_id': medicine,
        'match_present': match_present,
        'present_id': present_qs,
        'lab': match_lab,
        # 'revisit': revisit,
        'edit_visits_form': form,
    }
    return render(request, 'visits/edit_visit.html', context)


def table_visits(request):
    qs = list(Visits.objects.select_related('patient').order_by('-id')[:10])     # the next lines are the result of this query ORM
    # qs = Visits.objects.filter().order_by('-id')[:10]     # the next lines are the result of this query ORM
    # qs = Medicine.objects.select_related('patient').order_by('-id')
  
    inner1 = PresentHistory.objects.values('visit').filter(visit_id__in=qs)    #.exists()
    # # inner1 = PresentHistory.objects.values('visit').exclude(visit_id__in=qs).all()#.exists()
    # # inner1 = PresentHistory.objects.values_list('visit').filter(visit_id__in=qs)#.exists()
    # var0 = [obj['visit'] for obj in inner1]
    
    match_present = Visits.objects.filter(id__in=inner1)
    # match_present = PresentHistory.objects.filter(visit_id__in=visit)
    dict_visid = PresentHistory.objects \
                        .values('visit') \
                        .filter(visit_id__in=qs) 
                        # .annotate(ncount=Count('visit'))

    var = [item['visit'] for item in dict_visid]
    print(var, 'qs: ', qs)
    
    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = VisitsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=100)
    else:
        table = VisitsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)

    patname = request.GET.get('patname')
    patid   = request.GET.get('patid')
    visitid  = request.GET.get('visitid')
    visitdate  = request.GET.get('visitid')
    diagnosis  = request.GET.get('diagnosis')

    if patname == '' and diagnosis == '' and visitdate == '' and (patid == None or patid == '' or int(patid) == 0) and (visitid == None or visitid == '' or int(visitid) == 0):
        result_name = Visits.objects.all().order_by('-id')
        table = VisitsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('patname' in request.GET) and request.GET['patname'].strip():
        result_name = Visits.objects.filter(Q(patient__name__icontains=str(patname))).order_by('-visitdate')
        table = VisitsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('diagnosis' in request.GET) and request.GET['diagnosis'].strip():
        result_name = Visits.objects.filter(Q(diagnosis__icontains=str(diagnosis))).order_by('-visitdate')
        table = VisitsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('visitid' in request.GET) and request.GET['visitid']:
        result_name = Visits.objects.filter(Q(id=visitid)).order_by('-visitdate')
        table = VisitsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('visitdate' in request.GET) and request.GET['visitdate']:
        result_date = Visits.objects.filter(Q(visitdate=visitdate)).order_by('-visitdate')
        table = VisitsTable(result_date)
        table.paginate(page=request.GET.get("page", 1), per_page=10) 
    elif ('patid' in request.GET) and request.GET['patid']:
        result = Visits.objects.filter(Q(patient_id=patid)).order_by('-visitdate')
        table = VisitsTable(result)
        table.paginate(page=request.GET.get("page", 1), per_page=10)       


    # print(qs.query)
    context = {
        'qs_table': qs,
        'var': var, 
        # 'rec':rec,
        # 'records':records,
        'match_present': match_present,
        # 'inner1': inner,
        'visits_table': table,
    }
    return render(request, 'visits/tables.html', context)
# HttpResponse for http direct write

