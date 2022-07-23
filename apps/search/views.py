from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime, date
from django.contrib import messages
# from django.contrib.postgres.search import SearchVector

# from ..forms import PatientsForm, VisitsForm
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.patientdata.tables import PatientsTable
from apps.visits.tables import VisitsTable

# Create your views here.
def search_patient(request):
    patient_search = request.GET.get('q') # represent the text input in our form
    search_ph = request.GET.get('ph')
    search_id = request.GET.get('pid')
    search_card = request.GET.get('card')

    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        page_no = '10'
    else:
        page_no = request.GET.get('pageno')

    if patient_search == '' and search_ph == '' and (search_id == None or search_id == '' or int(search_id) == 0):
        result_id = Patients.objects.all().order_by('-id')
        table_search = PatientsTable(result_id)
        table_search.paginate(page=request.GET.get("page", 1), per_page=10)
        # print(str(patient_search)+ ' -both are "" ')
        # pass
        # messages.success(request, 'ID None Is Not Allowed')
        # return redirect('clinic:search')
    elif ('pid' in request.GET) and request.GET['pid']:
        result_id = Patients.objects.filter(Q(id=search_id)).all() # | Q(cardid__icontains=patient_search)
        table_search = PatientsTable(result_id)
    elif ('card' in request.GET) and request.GET['card']:#search_id != None:   # ('pid' in request.GET) and request.GET['pid']:
        result_id = Patients.objects.filter(Q(cardid=search_card)).all() # | Q(cardid__icontains=patient_search)
        table_search = PatientsTable(result_id)
    elif ('q' in request.GET) and request.GET['q'].strip():
        search_id = ''
        patient_search = request.GET.get('q')
        result_id = Patients.objects.filter(#Q(id=int(patient_search)) | 
                                            Q(name__icontains=str(patient_search)) |
                                            Q(address__icontains=str(patient_search))).all()
        # | Q(cardid__icontains=patient_search)
        table_search = PatientsTable(result_id)
        table_search.paginate(page=request.GET.get("page", 1), per_page=page_no)
        # print('ps not equal None ')
    elif search_ph:
        result_search = Patients.objects.filter(
            Q(phone__icontains=int(search_ph)) | Q(mobile__icontains=int(search_ph))).all()
        table_search = PatientsTable(result_search)
        table_search.paginate(page=request.GET.get("page", 1), per_page=page_no)
        # pass
    # elif patient_search = None:
    #     result_patient = Patients.objects.filter(
    #         Q(name__icontains=patient_search) | Q(address__icontains=patient_search))
    #     table_search = PatientsTable(result_patient)
    #     table_search.paginate(page=request.GET.get("page", 1), per_page=5)
        # print('ps not equal str ')

        # print('sph not equal None')
    # elif search_ph == '':
    #     result_id = Patients.objects.all().order_by('-id')
    #     table_search = PatientsTable(Patients.objects.all().order_by('-id'))
    #     table_search.paginate(page=request.GET.get("page", 1), per_page=15)
    #     print('sph not equal "" ')
    #     messages.success(request, 'Not Allowed phone empty')
    # elif patient_search == None:
    #     result_id = Patients.objects.all().order_by('-id')
    #     table_search = PatientsTable(result_id)
    #     table_search.paginate(page=request.GET.get("page", 1), per_page=15)
    #     print('ps equal ""')
    else:
        table_search = PatientsTable(Patients.objects.all().order_by('-id'))
        table_search.paginate(page=request.GET.get("page", 1), per_page=page_no)
        # messages.success(request, 'Not Allowed')
        # return redirect('/')   

    context = {
        'patient_search': patient_search,
        'table_patient_search':table_search,
    }
    return render(request, 'search/tables.html', context)


def search_visit(request):
    try:
        # patient_search = request.GET.get('q') # represent the text input in our form
        visit_search = request.GET.get('vis')      
        if visit_search.isnumeric():
            result_visit = Visits.objects.filter(Q(id=visit_search)).all()
            table_search = VisitsTable(result_visit,)
            table_search.paginate(page=request.GET.get("page", 1), per_page=5)
        elif visit_search == None:
            return redirect('search:search_visit')
        else:
            return redirect('/')
    except KeyError:
        return redirect('/')    

    context = {
        'table_search':table_search,
    }
    return render(request, 'search/tables.html', context)


def search_date(request):
    search_from = request.GET.get('from')
    search_to = request.GET.get('to')
    if (search_from) == '':
        return redirect('search:search_date')
    elif (search_to) == '':
        return redirect('search:search_date')
    elif search_from != '' and search_to != '':
        date_search = Visits.objects.filter(Q(visitdate__range=[search_from, search_to])).all().order_by('-visitdate')
        date_table_search = VisitsTable(date_search, exclude='addpresent, addrevis')
        date_table_search.paginate(page=request.GET.get("page", 1), per_page=5)
    # elif search_to != '':
    #     date_search = Visits.objects.filter(Q(visitdate__range=[search_from, search_to])).order_by('-visitdate')
    #     date_table_search = VisitsTable(date_search)
    #     date_table_search.paginate(page=request.GET.get("page", 1), per_page=5)
    else:
        date_search = Visits.objects.all().order_by('-visitdate')
        date_table_search = VisitsTable(date_search, exclude='addpresent, addrevis')
        date_table_search.paginate(page=request.GET.get("page", 1), per_page=25)
    
    context={ 
        'date_table_search':date_table_search,
    }
    return render(request, 'search/tables.html', context)


def search_only(request): # We need to know what this function do
    today = date.today()
    search_day = request.GET.get('day')
    search_month = request.GET.get('month')
    search_year = request.GET.get('year')
    if (search_day) == '' and (search_month) == '' and (search_year) == '':
        return redirect('search:search_date')
    elif search_day != '' and search_month != '' and search_year != '':
        date_search = Visits.objects.filter(Q(visitdate__year=search_year, visitdate__month=search_month, visitdate__day=search_day)).order_by('-id')
        date_table_search = VisitsTable(date_search, exclude='addpresent, addrevis')
        date_table_search.paginate(page=request.GET.get("page", 1), per_page=5)
    elif search_month != '' and search_year != '':
        date_search = Visits.objects.filter(Q(visitdate__year=search_year, visitdate__month=search_month)).order_by('-visitdate')
        date_table_search = VisitsTable(date_search, exclude='addpresent, addrevis')
        date_table_search.paginate(page=request.GET.get("page", 1), per_page=5)
    elif search_year != '':
        date_search = Visits.objects.filter(Q(visitdate__year=search_year)).order_by('-visitdate')
        date_table_search = VisitsTable(date_search, exclude='addpresent, addrevis')
        date_table_search.paginate(page=request.GET.get("page", 1), per_page=5)
    elif (search_year) == '':
        return redirect('search:search_date')
    elif (search_month) == '':
        pass
    elif (search_day) == '':
        pass
        # return redirect('search:search_date')
    else:
        date_search = Visits.objects.all().order_by('-visitdate')
        date_table_search = VisitsTable(date_search, exclude='addpresent, addrevis')
        date_table_search.paginate(page=request.GET.get("page", 1), per_page=25)
        
    
    context={ 
            'only_table_search':date_table_search,
            'search_day': search_day,
            'search_month': search_month,
            'search_year': search_year, 
            }
    return render(request, 'search/tables.html', context)


