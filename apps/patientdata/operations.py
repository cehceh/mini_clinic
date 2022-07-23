from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from datetime import date
import socket, pathlib, sys
from django.core.exceptions import PermissionDenied

from .models import Patients, Operations
from .forms import OperationsForm
from .tables import OperationsTable
from .views import auth_required

# pathlib.Path('C:/G/mypackage/', 'myfile')

# sys.path.insert(0, '/EtmanClinic/clenv/Lib/')
# sys.path.append('/EtmanClinic/clenv/Lib/')

# sys.path.insert(1, pathlib.Path('/G/mypackage/myfile.py'))
# sys.path.insert(1, r'C:/G/mypackage/')
# path = pathlib.Path(my_out_dir, 'myfile.py')
# from my_out_dir import auth_required
# from Lib.mypackage.myfile import auth_required


def save_operation(request, patient_id):
    patient = Patients.objects.get(id=patient_id)
    if request.method == 'POST':
        form = OperationsForm(request.POST)
        # print(form)
        if form.is_valid():
            # print('valid form')
            save_form = form.save(commit=False)
            save_form.patient_id = patient_id
            save_form.save()
            messages.success(request, 'Saving Operation Details Done ... ')
            return redirect(reverse('patientdata:edit_operation', kwargs={
                'patient_id':patient_id, 'id': save_form.id,
            }))
    else:
        form = OperationsForm()
        # messages.error(request, 'Failed To Save Operation Details !!! ')

    context = {
        'form': form,
        'patient': patient,
        'patient_id': patient_id, 
    }
    return render(request, 'patientdata/save_operation.html', context)


def edit_operation(request, patient_id, id):
    patient = Patients.objects.get(id=patient_id)
    
    qs = Operations.objects.get(id=id)
    form = OperationsForm(request.POST or None, instance=qs)

    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.patient_id = patient_id
        save_form.save()
    
    context = {
        'form': form,
        'patient': patient,
    }
    return render(request, 'patientdata/edit_operation.html', context)

@auth_required
def operation_table(request):
    # my_out_dir = 'C:/G/mypackage/'

    # append = sys.path.append(my_out_dir)
    # append1 = sys.path.append('/EtmanClinic/')
    # insert = sys.path.insert(1, 'C:/G/mypackage/')
    # print(append1, my_out_dir, insert)
    # remote_address = request.META.get('REMOTE_ADDR')
    # my_addr = request.get_host()#request._current_scheme_host
    # hostname = socket.gethostname() 
    # ip = socket.gethostbyname(hostname)
    # # my_ip = '127.0.0.1'
    # ip1 = '192' + '.' + '168' + '.' + '1' + '.' + '55' #remote_address
    # print('myaddress=', my_addr, ' my machine name=',hostname, ' ip=',ip, ' the_remote_ip',remote_address)

    # if remote_address == ip: 
    #     qs = Operations.objects.filter(opdate__gte=date.today()).all().order_by('-opdate') 
    # elif remote_address == ip1 and ip: 
    #     qs = Operations.objects.filter(opdate__gte=date.today()).all().order_by('-opdate')
    # elif remote_address != ip1 and not ip:
    #     from django.http import Http404
    #     raise Http404
    # else:
    #     # print('not alowed')
    #     qs = None#Operations.objects.filter(opdate__gte=date.today()).all().order_by('-opdate')
    #     raise Http404 #PermissionDenied
    
    qs = Operations.objects.filter(opdate__gte=date.today()).all().order_by('-opdate')
    # table = OperationsTable(qs)

    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = OperationsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif page_no != None or page_no != '' or int(page_no) != 0:
        table = OperationsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
    else:
        table = OperationsTable(qs)
        table.paginate(page=request.GET.get("page", 1), per_page=10) 

    patname = request.GET.get('patname')
    patid   = request.GET.get('patid')
    opname  = request.GET.get('opname')
    opdate  = request.GET.get('opdate')

    if patname == '' and opname == '' and opdate == '' and (patid == None or patid == '' or int(patid) == 0):
        # result_name = Operations.objects.all().order_by('-id')
        result_name = Operations.objects.filter(opdate__gte=date.today()).all().order_by('-id')
        table = OperationsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('patname' in request.GET) and request.GET['patname'].strip():
        result_name = Operations.objects.filter(Q(patient__name__icontains=str(patname))).order_by('-opdate')
        table = OperationsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('opname' in request.GET) and request.GET['opname'].strip():
        result_name = Operations.objects.filter(Q(name__icontains=str(opname))).order_by('-opdate')
        table = OperationsTable(result_name)
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('opdate' in request.GET) and request.GET['opdate']:
        result_date = Operations.objects.filter(Q(opdate=opdate)).order_by('-opdate')
        table = OperationsTable(result_date)
        table.paginate(page=request.GET.get("page", 1), per_page=10) 
    elif ('patid' in request.GET) and request.GET['patid']:
        result_date = Operations.objects.filter(Q(patient_id=patid)).order_by('-opdate')
        table = OperationsTable(result_date)
        table.paginate(page=request.GET.get("page", 1), per_page=10)       


    context = {
        'operation_table': table,
    }
    return render(request, 'patientdata/operation_table.html', context)


# def test_path(request):




