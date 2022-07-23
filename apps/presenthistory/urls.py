from django.urls import path
from .views import *


app_name = "presenthistory"
urlpatterns = [

    # Present History section
    path('create/present/history/patient/<int:patient_id>/visit/<int:visit_id>/',
        save_present_hist,
        name='save_present_hist'),

    path('present/history/patient/<int:patient_id>/visit/<int:visit_id>/edit/<int:id>/', 
        edit_present_hist, 
        name="edit_present_hist"),   

    path('present/history/table/',
        table_present_hist,
        name='table_present_hist'),
    #
    path('delete/present/history/<int:id>/',
        delete_history, 
        name="delete_history"),

    #
    path('present/history/patient/<int:patient_id>/',
        patient_history_table,
        name="patient_history_table"),
    #
    path('present/history/visit/<int:visit_id>/',
        visit_history_table, 
        name="visit_history_table"),

    #
    path('add/present/history/', 
        table_add_present_hist, 
        name="table_add_present_hist"),

]