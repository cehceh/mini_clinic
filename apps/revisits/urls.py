from django.urls import path
from .views import *

app_name= "revisits"

urlpatterns = [
     path('create/revisit/patient/<int:patient_id>/visit/<int:visit_id>/',
        save_revisit,
        name='save_revisit'),
    #
    path('edit/revisit/<int:id>/patient/<int:patient_id>/visit/<int:visit_id>/', 
        edit_revisit, 
        name='edit_revisit'),    
    #
    path('table/revisits/', 
        table_revisit, 
        name='table_revisit'),
    #
    path('table/for/visit/<int:visit_id>/patient/<int:patient_id>/', 
        view_revisit, 
        name='view_revisit'),
    #
    path('delete/revisit/<int:id>/',
        delete_revisit, 
        name="delete_revisit"),
]