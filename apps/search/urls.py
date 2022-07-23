from django.urls import path
from .views import *

app_name= "search"

urlpatterns = [

    #
    path('search/patient/', search_patient, name='search_patient'),
    path('search/visit/', search_visit, name='search_visit'),
    path('search/date/', search_date, name='search_date'),
    path('search/only/date/', search_only, name='search_only'),

    #
    # path('income/day/<int:day>/<int:month>/<int:year>/', calculate_income, name='day_income'),
    # path('income/month/<int:day>/<int:month>/<int:year>/', calculate_income, name='month_income'),
    
    # path('income/year/<int:year>/', calculate_income, name='year_income'),
    
    # path('income/day/', calculate_income, name='calculate_day_income'),
    # path('income/month/', calculate_income, name='calculate_month_income'),
    
    # path('income/day/', calculate_day_income, name='calculate_day_income'),
    # path('income/month/', calculate_month_income, name='calculate_month_income'),
    # path('income/year/', calculate_year_income, name='calculate_year_income'),
    

]