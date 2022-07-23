from django.urls import path
from .views import *
from .prescription import *
app_name= "visitdrug"

urlpatterns = [
    #
    path('prescription/for/patient/<int:patient_id>/visit/<int:visit_id>/',
        save_medicine, name='save_medicine'),
    #
    path('add/prescription/for/patient/<int:patient_id>/visit/<int:visit_id>/',
        add_new, name='add_new'),
    #
    path('patient/<int:patient_id>/visit/<int:visit_id>/drug/<int:id>/', 
        edit_medicine, name='edit_medicine'),
    #
    path('patient/<int:patient>/visit/<int:visit>/delete/drug/<int:id>/', delete_medicine, name='delete_medicine'),
    path('table/medicine/', table_medicine, name='table_medicine'),
    
    #
    # path('prescription/visit/<int:visit_id>/', get_pdf, name='get_pdf'),
    
    # This is a good one for printing prescription
    path('print/visit/<int:visit_id>/', print_html, name='print_html'),
    #
    
]