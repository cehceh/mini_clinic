from django.urls import path
from .views import save_pasthist, edit_pasthist, pasthist_table, delete_pasthist


# APP_NAME='pasthistory'
app_name='pasthistory'
urlpatterns = [
   # add past history
    path('create/past/history/patient/<int:patient_id>/', 
        save_pasthist, 
        name='save_pasthist'),
   
    #
    path('past/history/patient/<int:patient_id>/edit/<int:id>/', 
        edit_pasthist, 
        name='edit_pasthist'),
    
    #
    path('past/history/table/', pasthist_table, name='pasthist_table'),
    
    #
    path('delete/past/history/<int:id>/', delete_pasthist, name='delete_pasthist'),
    
]