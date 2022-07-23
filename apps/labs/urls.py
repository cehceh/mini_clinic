from django.urls import path
from .views import (
                    # add_lab_followup, edit_lab_followup,lab_followup_table,
                    add_lab_visit, edit_lab_visit,lab_visit_table,
                    delete_lab_visit)

from .prescription import print_html

app_name = 'labs'
urlpatterns = [
    path('add/visit/lab/for/patient/<int:patient_id>/visit/<int:visit_id>/', 
        add_lab_visit, name='add_lab_visit'),
    path('edit/visit/lab/<int:lab_id>/patient/<int:patient_id>/visit/<int:visit_id>/',
        edit_lab_visit, name='edit_lab_visit'),
    path('add/visits/lab/table/',
        lab_visit_table, name='lab_visit_table'),
    path('delete/visit/lab/<int:lab_id>/patient/<int:patient_id>/visit/<int:visit_id>/',
        delete_lab_visit, name='delete_lab_visit'),

    # path('add/lab/for/patient/<int:patient_id>/followup/visit/<int:followup_id>/', 
    #     add_lab_followup, name='add_lab_followup'),
    # path('edit/lab/<int:lab_id>/patient/<int:patient_id>/followup/visit/<int:followup_id>/',
    #     edit_lab_followup, name='edit_lab_followup'),
    
    # path('table/for/add/followup/visit/', 
    #     delete_lab_visit, name='delete_lab_visit'),

    path('prescription/analysis/for/visit/<int:visit_id>/',
        print_html, name='print_html'),
    
]
