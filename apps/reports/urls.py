from django.urls import path

from .views import (
    calculate_income, calculate_day_income, print_html,
    calculate_month_income, calculate_year_income,
    # getpdf, get_pdf, print_pdf, 
    fast_print
)


app_name = 'reports'
urlpatterns = [
    path('income/year/<int:year>/', calculate_income, name='year_income'),
    # path('income/day/', calculate_income, name='calculate_day_income'),
    path('print/year/report/', print_html, name='print_html'),
    path('fast/print/', fast_print, name='fast_print'),
    # for test export to pdf
    # path('print/preview/export/to/pdf/', getpdf, name='getpdf'),
    # path('justin/export/to/pdf/', get_pdf, name='get_pdf'),
    # path('stack/export/pdf/', print_pdf, name='print_pdf'),
    
    path('income/day/', calculate_day_income, name='calculate_day_income'),
    path('income/month/', calculate_month_income, name='calculate_month_income'),
    path('income/year/', calculate_year_income, name='calculate_year_income'),
    
]





