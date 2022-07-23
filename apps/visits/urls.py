from django.urls import path  
from .views import *


app_name = 'visits'
urlpatterns = [
  
    # for visit
    path('create/visit/patient/<int:id>/', 
        pass_patient_id, name='pass_patient_id'),
    path('edit/visit/<int:id>/patient/<int:patient_id>/', 
        visits_patient_id, name='visits_patient_id'),
    
    # path('edit/visit/<int:id>/', visits.edit_visits, name='edit_visits'),
    path('table/list/all/visits/', table_visits, name='table_visits'),
    path('export/table/', export_table, name='export_table'),
   
]