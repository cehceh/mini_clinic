from django.urls import path  # defs
# from clinic.views.home import homepage
from .views import (save_patient, edit_patient, table_patient)
from .operations import save_operation, edit_operation, operation_table
# from clinic.views import visits, medicine, prescription
# from clinic.views.search import search_patient, search_visit, search_date, search_only
# from clinic.views.calculations import (calculate_income, calculate_day_income, 
#                                         calculate_month_income, calculate_year_income)

app_name = 'patientdata'
urlpatterns = [

    # for patient
    path('create/patient/', save_patient, name='save_patient'),
    path('edit/patient/<int:id>/', edit_patient, name='edit_patient'),
    path('table/patients/', table_patient, name='table_patient'),
    # path('patient/details/by/barcode/<str:barcode>/', patient_details, name='patient_details'),
    
    # for operations
    path('add/operation/details/<int:patient_id>/', save_operation, name='save_operation'),
    path('add/operation/details/for/patient/<int:patient_id>/id/<int:id>/', edit_operation, name='edit_operation'),
    path('operation/table/', operation_table, name='operation_table'),
    
    # path('edit/visit/<int:id>/', visits.edit_visits, name='edit_visits'),
    # path('table/visits/', visits.table_visits, name='table_visits'),
    # path('export/table/', visits.export_table, name='export_table'),

    #
    # path('drug/patient/<int:patient_id>/visit/<int:visit_id>/',
    #     medicine.save_medicine, name='save_medicine'),
    #
    # path('add/prescription/patient/<int:patient_id>/visit/<int:visit_id>/',
    #     medicine.add_new, name='add_new'),
    #
    # path('patient/<int:patient_id>/visit/<int:visit_id>/drug/<int:id>/', 
    #     medicine.edit_medicine, name='edit_medicine'),
    
    #
    # path('patient/<int:patient>/visit/<int:visit>/delete/drug/<int:id>/', medicine.delete_medicine, name='delete_medicine'),
    # path('table/medicine/', medicine.table_medicine, name='table_medicine'),
    
    #
    # path('search/patient/', search_patient, name='search_patient'),
    # path('search/visit/', search_visit, name='search_visit'),
    # path('search/date/', search_date, name='search_date'),
    # path('search/only/date/', search_only, name='search_only'),

    #
    # path('income/day/<int:day>/<int:month>/<int:year>/', calculate_income, name='day_income'),
    # path('income/month/<int:day>/<int:month>/<int:year>/', calculate_income, name='month_income'),
    # path('income/year/<int:year>/', calculate_income, name='year_income'),
    # # path('income/day/', calculate_income, name='calculate_day_income'),
    # # path('income/month/', calculate_income, name='calculate_month_income'),
    # path('income/day/', calculate_day_income, name='calculate_day_income'),
    # path('income/month/', calculate_month_income, name='calculate_month_income'),
    # path('income/year/', calculate_year_income, name='calculate_year_income'),
    
    # #
    # path('prescription/visit/<int:visit_id>/', prescription.get_pdf, name='get_pdf'),
    # # This is a good one for printing prescription
    # path('print/visit/<int:visit_id>/', prescription.print_html, name='print_html'),
    # #
    # path('pdf/', prescription.some_view, name='some_view'),

]   
