from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q, Max
from django.db import connection, transaction
from django.contrib import messages
from datetime import datetime, date
# from django.contrib.postgres.search import SearchVector

from apps.patientdata.forms import PatientsForm
from apps.patientdata.models import Patients
from apps.visits.forms import VisitsForm
from apps.visits.models import Visits
from apps.patientdata.tables import PatientsTable
from apps.visits.tables import VisitsTable

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def calculate_day_income(request):
    today = date.today()#datetime.now()

    day_income = Visits.objects.filter(visitdate__year=today.year, 
                                        visitdate__month=today.month,
                                        visitdate__day=today.day)
    table = VisitsTable(day_income, exclude='addpresent')
    table.paginate(page=request.GET.get("page", 1), per_page=3)
    # print(day_income)
    search_name = request.GET.get('name')
    search_vis = request.GET.get('vis')
    search_date = request.GET.get('d')
    search_dia = request.GET.get('dia')
    if search_name == None and search_vis == None and search_date == None and search_dia== None: 
        table = VisitsTable(day_income, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('vis' in request.GET) and request.GET['vis']:#search_vis != '':
        visit = Visits.objects.filter(Q(id=search_vis,
                                        visitdate__year=today.year, 
                                        visitdate__month=today.month, visitdate__day=today.day))
        table = VisitsTable(visit, exclude='addpresent')
        # table.paginate(page=request.GET.get("page", 1), per_page=5)
    elif ('d' in request.GET) and request.GET['d']: 
        result_date = Visits.objects.filter(Q(visitdate=search_date))
        table = VisitsTable(result_date, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('name' in request.GET) and request.GET['name'].strip():#
        patient = Visits.objects.filter(Q(patient__name__icontains=search_name,
                                        visitdate__year=today.year, visitdate__month=today.month, visitdate__day=today.day)) # note HERE '__name__icontains' it's important to get related field "patient"(string not id) 
        table = VisitsTable(patient, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('dia' in request.GET) and request.GET['dia']: 
        result_dia = Visits.objects.filter(Q(diagnosis=search_dia, visitdate__year=today.year, visitdate__month=today.month, visitdate__day=today.day))
        table = VisitsTable(result_dia, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    # elif search_vis == "" or int(search_vis) == 0: 
    #     table = VisitsTable(month_income, exclude='addpresent')
    #     table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = VisitsTable(day_income, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    
    context = {
            'day_table': table,
    }
    return render(request, 'reports/day_table.html', context)


def calculate_month_income(request):
    today = date.today()       # datetime.now()
    month_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month)
    table = VisitsTable(month_income, exclude='addpresent')
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    
    income = Visits.objects.values('visitdate').filter(visitdate__year=2020, visitdate__month=12)
    print(income, income[0], income[0]['visitdate'], income[0]['visitdate'].month)

    search_name = request.GET.get('name')
    search_vis = request.GET.get('vis')
    search_dia = request.GET.get('dia')
    search_month = request.GET.get('month')
    if search_name == None and search_vis == None and search_dia == None and search_dia == None and search_month == None: 
        table = VisitsTable(month_income, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('vis' in request.GET) and request.GET['vis']:
        visit = Visits.objects.filter(Q(id=search_vis, visitdate__year=today.year, visitdate__month=today.month))
        table = VisitsTable(visit, exclude='addpresent')
    elif ('month' in request.GET) and request.GET['month']:
        result_month = Visits.objects.filter(Q(visitdate__year=today.year, visitdate__month=search_month))
        table = VisitsTable(result_month, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=5)
    elif ('dia' in request.GET) and request.GET['dia']: 
        result_dia = Visits.objects.filter(Q(diagnosis__icontains=search_dia, visitdate__year=today.year, visitdate__month=today.month))
        table = VisitsTable(result_dia, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    elif ('name' in request.GET) and request.GET['name'].strip():#
        patient = Visits.objects.filter(Q(patient__name__icontains=search_name,
                                        visitdate__year=today.year, visitdate__month=today.month)) # note HERE '__name__icontains' it's important to get related field "patient"(string not id) 
        table = VisitsTable(patient, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    else:
        table = VisitsTable(month_income, exclude='addpresent')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
    
    context = {
        'month_table': table,
    }
    return render(request, 'reports/month_table.html', context)


def calculate_year_income(request):
    today = date.today()#datetime.now()
    # income = Visits.objects.all()
    # table = VisitsTable(income)
    # table.paginate(page=request.GET.get('page', 1), per_page=10)

    year_income = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
    year_table = VisitsTable(year_income, exclude='addpresent')
    year_table.paginate(page=request.GET.get("page", 1), per_page=10)
    
    print_table = VisitsTable(year_income, exclude='addpresent, addlab, addrevis')
    print_table.paginate(page=request.GET.get("page", 1), per_page=10)

    context = {
        'year_table': year_table,
        'print_table': print_table,
    }
    return render(request, 'reports/year_table.html', context)



def calculate_income(request, year):
    today = date.today()#datetime.now()
    day = today.day
    month = today.month
    year = today.year
    # income = Visits.objects.all()
    # table = VisitsTable(income)
    # table.paginate(page=request.GET.get('page', 1), per_page=10)
    # if day is not None and month is not None and year is not None:
    #     day_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month, visitdate__day=today.day)
    #     table = VisitsTable(day_income)
    #     table.paginate(page=request.GET.get("page", 1), per_page=2)
    #     return redirect(reverse('clinic:day_income', args=(today.day, today.month, today.year)))
    # elif month is not None and year is not None:
    #     month_income = Visits.objects.filter(visitdate__year=today.year, visitdate__month=today.month)
    #     table = VisitsTable(month_income)
    #     table.paginate(page=request.GET.get("page", 1), per_page=3)
    #     return redirect(reverse('clinic:month_income', args=(today.month, today.year)))
    # if year != None:
    cal_year = Visits.objects.values('visitdate').filter(visitdate__year=year).first()
    year_value = cal_year['visitdate']
    # print(cal_year, year_value)
    year_income = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
    table = VisitsTable(year_income, exclude='addpresent')
    table.paginate(page=request.GET.get("page", 1), per_page=5)
    return redirect('/clinic/income/year/'+ str(year_value.year) +'/')
    
    context = {
        'income_table': table,
    }
    return render(request, 'tables.html', context)


# This method to print prescription
def print_html(request):
    today = date.today()#datetime.now()
    qs = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
    table = VisitsTable(qs, exclude='addpresent, addlab, addrevis, diagnosis,')
    # table.paginate(page=request.GET.get("page", 1), per_page=5)
    
    page_no = request.GET.get('pageno')
    if page_no == None or page_no == '' or int(page_no) == 0:
        table = VisitsTable(qs, exclude='addpresent, addlab, addrevis, diagnosis,')
        table.paginate(page=request.GET.get("page", 1), per_page=10)
        # paginator = Paginator(qs, 10) 
        # page = request.GET.get('page')
        # try:
        #     qs_page = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer deliver the first page
        #     qs_page = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range deliver last page of results
        #     qs_page = paginator.page(paginator.num_pages)
        # qs = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
        
    elif page_no != None or page_no != '' or int(page_no) != 0:
        table = VisitsTable(qs, exclude='addpresent, addlab, addrevis, diagnosis,')
        table.paginate(page=request.GET.get("page", 1), per_page=page_no)
        # paginator = Paginator(qs, page_no) 
        # page = request.GET.get('page')
        # try:
        #     qs_page = paginator.page(page)
        # except PageNotAnInteger:
        #     # If page is not an integer deliver the first page
        #     qs_page = paginator.page(page_no)
        # except EmptyPage:
        #     # If page is out of range deliver last page of results
        #     qs_page = paginator.page(paginator.num_pages)
        # qs = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
        
    # else:
    #     ## next lines for paginate all 
    #     paginator = Paginator(qs, page_no) 
    #     page = request.GET.get('page')
    #     try:
    #         qs_page = paginator.page(page)
    #     except PageNotAnInteger:
    #         # If page is not an integer deliver the first page
    #         qs_page = paginator.page(1)
    #     except EmptyPage:
    #         # If page is out of range deliver last page of results
    #         qs_page = paginator.page(paginator.num_pages)
    
    
    context = {
        'visit_table': table,
        'qs': qs,
        # 'qs_page': qs_page,
        # 'page': page,
    }
    return render(request, 'reports/print.html', context)

def fast_print(request):
    # return redirect(reverse('reports:print_html'))
    return render(request, 'reports/print.html', {})

###############################################################
# import arabic_reshaper
# from bidi.algorithm import get_display

# '''#...
# reshaped_text = arabic_reshaper.reshape(u'اللغة العربية رائعة')
# bidi_text = get_display(reshaped_text)
# pass_arabic_text_to_render(bidi_text)  # <-- This function does not really exist
# #...'''

# # import reshaper
# from io import BytesIO
# import os
# from bidi.algorithm import get_display
# from reportlab.pdfgen import canvas
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib.units import inch 
# from reportlab.lib.pagesizes import letter

# # from reportlab.platypus import SimpleDocTemplate, Paragraph
# import reportlab
# from django.conf import settings
# from reportlab.pdfbase import pdfmetrics
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.pdfbase.ttfonts import TTFont

# # import reshaper
# from bidi.algorithm import get_display
# # from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.platypus.tables import Table
# from reportlab.pdfbase import pdfmetrics
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.pdfbase.ttfonts import TTFont



# ### https://codingisfuture.com/page/3/
# from reportlab.pdfgen import canvas  
# from django.http import HttpResponse 

# def getpdf(request):  
#     cm = 2.54
#     path = (str(settings.STATIC_ROOT)+'/fonts/')
#     arabic_text = arabic_reshaper.reshape(u'العربية')
#     arabic_text = get_display(arabic_text)
#     pdfmetrics.registerFont(TTFont('Arabic-bold', str(path)+'/Amiri-Regular.ttf'))
    
#     today = date.today()#datetime.now()
#     qs = Visits.objects.filter(visitdate__year=today.year).order_by('-id')
#     project = Visits.objects.filter()
#     # final_products = ', '.join(list(project.values_list('patient')[0]))

#     projects_list = list(qs.values_list(
#                             'id', (arabic_reshaper.reshape('patient__name')), 'visitdate',
#                             'amount',))
#     print(projects_list)
#     all_fields = [] 

#     # for i in range(len(projects_list)):
#     #     value= projects_list[i]
    
#     #     # if i == 0:        
#     #     #     value= Project.MATURITY[value-1][1]
#     #     # if i in [ 12]:        
#     #     #     value= Project.CHOICES[value-1][1]
#     #     # if i  in [ 9 ,18,20]:        
#     #     #     value= Project.YES_NO[value-1][1]
#     #     all_fields.append(get_display(arabic_reshaper.reshape(str(value))))
    
#     all_fields.append(get_display(arabic_reshaper.reshape(str(qs))))
#     # init the buffer
#     buffer = BytesIO()
    
#     #new font
#     reportlab.rl_config.TTFSearchPath.append(str(settings.STATIC_ROOT)+'/fonts/')
#     # path = (str(settings.STATIC_ROOT)+'/fonts/')
#     pdfmetrics.registerFont(TTFont('Arabic', str(path)+'/Amiri-Regular.ttf'))
    
#     #styling the pdf
#     styles = getSampleStyleSheet()
#     styleN = styles['Normal']
#     styleH_1 = ParagraphStyle(
#         'heading3_arab',
#         parent = styles['Heading1'],
#         fontName="Arabic"
        
#         )

#     styleH_2 = styles['Heading2']
#     styleH_3 = ParagraphStyle(
#         'heading3_arab',
#         parent = styles['Heading3'],
#         fontName="Arabic"
        
#         )

#     styleBorder = ParagraphStyle(
#         'border',
#         parent = styleN ,
#         borderColor= '#333333',
#         borderWidth =  1,
#         borderPadding  =  2,
#         fontName="Arabic"
#     )

#     styleBorderH2 = ParagraphStyle(
#         'borderH2',
#         parent = styleH_2 ,
#         borderColor= '#333333',
#         borderWidth =  1,
#         borderPadding  =  2,
#         fontName="Arabic"
#     )
#     story = []

#     #add the header and the project name
#     arabic_text = arabic_reshaper.reshape("السلام عليكم")
#     # story.append(arabic_reshaper.reshape("السلام عليكم"))
#     story.append(Paragraph(get_display(arabic_text),styleH_1))
#     story.append(Paragraph("This is adraft of a business plan for your idea or project.",styleN))
#     story.append(Spacer(1,8))
#     # project_name = arabic_reshaper.reshape(list(qs.values_list('patient__name', flat=True))[0])#[0]list
#     # project_name = arabic_reshaper.reshape(list(qs.values_list('patient__name', flat=True))[0])#[0]list
#     project_name = arabic_reshaper.reshape(str(all_fields))#[0]list
#     story.append(Paragraph(get_display(project_name),styleBorderH2))
#     story.append(Spacer(1,8))  

    
#     titles = []
#     elements = []
#     #add the data to pdf
#     # for title, data in zip(titles, all_fields):
        
#     #     story.append(Paragraph(title,styleH_3))
#     #     story.append(Spacer(1,5))
#     #     story.append(Paragraph(str(data),styleBorder))
#     #     story.append(Spacer(1,25))

#     #create the doc
#     # doc = SimpleDocTemplate(buffer, pagesize=letter)
#     doc = SimpleDocTemplate(buffer, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
#     table = Table((projects_list), colWidths=170, rowHeights=30)
#     elements.append(table)
#     doc.build(elements)
#     # doc.build(story)

#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)

#     return response
#     # return pdf
#     # return project_name ,pdf
#     # response = HttpResponse(content_type='application/pdf')  
#     # response['Content-Disposition'] = 'attachment; filename="get_file.pdf"'  
#     # p = canvas.Canvas(response)  
#     # p.setFont("Times-Roman", 25)  
    
#     # p.drawString(100,700, "Hello, Python Decoders\n Family.\n كيف حالك")  
#     # p.showPage()  
#     # p.save()  
#     # return response

# from typing import ContextManager  
# from django.http import HttpResponse
# from django.template.loader import get_template
# from bidi import algorithm as bidialg
# from xhtml2pdf import pisa
# import time

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()

#     ''' important notes about rendring html to pdf via 'pisa' next three lines are working good to fix the problem
#     of Arabic language except the letters are separated 
#     '''
#     # arabic_reshaper.reshape
#     arabic = arabic_reshaper.reshape(str(html))

#     pdf = pisa.CreatePDF(bidialg.get_display(arabic, base_dir="L"), result, encoding='utf8') #iso-8859-6, CreatePDF = pisaDocument
#     # pdf = pisa.pisaDocument(BytesIO(get_display(html.encode('utf-8'))), result)
#     # pdf = pisa.pisaDocument(BytesIO(bidialg.get_display(html.encode('utf-8'), base_dir='L')), result)
#     # pdf = pisa.pisaDocument(bidialg.get_display((arabic), base_dir='L'), result)
#     # pdf = pisa.pisaDocument(bidialg.get_display(html.encode('UTF-8')), result)
    
#     # pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), result) #

#     # pdf = pisa.pisaDocument(BytesIO(html.encode("iso-8859-6")), result)
#     # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        
#     # print(type(html.encode('utf8')))#(var.encode('utf8'))
#     # print((bytes(b,'utf-8')))
#     # https://stackoverflow.com/questions/60139294/rendering-pdf-template-in-django-in-arabic-language
#     # pdf = pisa.pisaDocument(BytesIO(html.encode('cp1252')), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None

# #This is func based to render to pdf Justin code
# def get_pdf(request, *args, **kwargs):
#     # vis_id = Visits.objects.get(id=visit_id)
#     # qs = Medicine.objects.filter(visit=visit_id).order_by('-id')
#     # plan = Medicine.objects.values('plan').filter(visit=visit_id).first()
#     # plan1 = Medicine.objects.filter(plan=plan['plan'])
#     # vdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
#     # visitdate = vdate['visitdate']

#     # patname = Medicine.objects.values('patient').filter(visit=visit_id).first()
#     # patient = Patients.objects.get(id=patname['patient'])#patname['patient']

#     # print(patient , plan1)
#     # plan = qs1['plan']
#     # for obj in plan:
#         # print(obj['plan'])
#         # p = obj['plan'] #araby.tokenize()
#         # return p   

#     qs = Visits.objects.all().order_by('-id')
#     projects_list = list(qs.values_list(
#                             'id', 'patient__name', 'visitdate',
#                             'amount',))
    
#     all_fields = [] 

#     for i in range(len(projects_list)):
#         value= projects_list[i]
#         all_fields.append(get_display(arabic_reshaper.reshape(str(value))))
    
#     arabic_qs = arabic_reshaper.reshape(str(projects_list))
#     var = get_display(arabic_qs)
#     # var  = get_display(var1)
    
#     # all_fields
#     print(var)
#     # zero_remain = LaundryBill.objects.filter(sumtotal__gt=0, returns=False, remain=0).order_by('-id')
    
#     template = get_template('reports/pdf.html')
#     title1 = get_display(arabic_reshaper.reshape(u'التقارير'))
#     pdf_title = get_display(arabic_reshaper.reshape(u'عرض الملفات')) 
#     context = { 
#         # 'p': p,
#         'qs': qs,
#         "all_fields":all_fields,
#         # "visit_no": vis_id,
#         "var": var,
#         "title1": title1,
#         "title": pdf_title,
#     }
#     html = template.render(context)
#     pdf = render_to_pdf('reports/pdf.html', context)
#     if pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "Prescription_"+str(time.strftime('%d-%m-%Y'))+".pdf" #%('%Y-%m-%d')
#         content = "inline; filename=%s" %(filename)
#         download = request.GET.get("download")
#         if download:
#             content = "attachment; filename='%s'" %(filename)
#         response['Content-Disposition'] = content
#         return response
#     return HttpResponse(pdf, content_type='application/pdf')

# # https://stackoverflow.com/questions/3372885/how-to-make-a-simple-table-in-reportlab
# from reportlab.platypus import SimpleDocTemplate
# # from reportlab.platypus.tables import Table, TableStyle
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# cm = 2.54

# def print_pdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

#     elements = []
#     buffer = BytesIO()

#     doc = SimpleDocTemplate(buffer, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
#     # doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
#     arabic = get_display(arabic_reshaper.reshape('العدد'))
#     data=[(arabic, 2),(3,4)]
#     table = Table((data), colWidths=270, rowHeights=79)
#     table.setStyle(TableStyle(
#     [('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#         ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
#         ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
#         ('BACKGROUND', (0, 0), (-1, 0), colors.gray)]))
#     elements.append(table)
#     doc.build(elements)

#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#     return response
# ### from https://simpleisbetterthancomplex.com/tutorial/2016/08/08/how-to-export-to-pdf.html
# # from io import BytesIO
# # from reportlab.pdfgen import canvas
# # from django.http import HttpResponse

# # def getpdf(request):
# #     response = HttpResponse(content_type='application/pdf')
# #     response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

# #     buffer = BytesIO()
# #     p = canvas.Canvas(buffer)

# #     # Start writing the PDF here
# #     p.drawString(100, 100, 'Hello world.سلام')
# #     # End writing

# #     p.showPage()
# #     p.save()

# #     pdf = buffer.getvalue()
# #     buffer.close()
# #     response.write(pdf)

# #     return response
# #######################################################

# ## Using ReportLab
# # def save_startup_pdf(user_pk=None, project_pk=None):
# #     # get the data
# #     project = Project.objects.filter(owner__user__id=user_pk,id=project_pk)
# #     final_products = ', '.join(list(Project.objects.get(owner__user__id=user_pk,id=project_pk).final_product.values_list('name')[0]))

# #     projects_list = list(project.values_list(
# #                             'maturity', 'details', 'category__name','custome_category', 
# #                             'custome_final_product','team_members', 'budget', 'pervious_financing__name_f', 'generate_money',
# #                             'have_picture', 'business_plan', 'timeline', 'have_prototype','ready_video', 'extension', 'similar_product', 'price', 
# #                             'unique_description', 'market_research', 'equity', 'patent' ))[0]
    
# #     all_fields = [] 

# #     for i in  range(len(projects_list)) :
# #         value= projects_list[i]
    
# #         if i == 0:        
# #             value= Project.MATURITY[value-1][1]
# #         if i in [ 12]:        
# #             value= Project.CHOICES[value-1][1]
# #         if i  in [ 9 ,18,20]:        
# #             value= Project.YES_NO[value-1][1]

# #         all_fields.append(get_display(arabic_reshaper.reshape(str(value))))
# #     all_fields.append(get_display(arabic_reshaper.reshape(str(final_products))))

# #     titles = []

    
# #     for field in Project._meta.get_fields():    
# #         if field.name not in ['id', 'owner', 'project_id', 'name','presentation' , 'stars','diamondsreview',
# #                             'diamonds', 'accepted', 'date', 'comment', 'teammembers', 'starsreview']:
    
# #             titles.append(get_display(arabic_reshaper.reshape(str(field.verbose_name.title()))))  

# #     # init the buffer
# #     buffer = BytesIO()
    
# #     #new font
# #     reportlab.rl_config.TTFSearchPath.append(str(settings.STATIC_ROOT)+'/home/fonts/')
# #     path = Path(str(settings.STATIC_ROOT)+'/home/fonts/')
# #     pdfmetrics.registerFont(TTFont('Arabic', str(path)+'/29ltbukraregular.8867a5331cd7.ttf'))
    
# #     #styling the pdf
# #     styles = getSampleStyleSheet()
# #     styleN = styles['Normal']
# #     styleH_1 = ParagraphStyle(
# #         'heading3_arab',
# #         parent = styles['Heading1'],
# #         fontName="Arabic"
        
# #         )

# #     styleH_2 = styles['Heading2']
# #     styleH_3 = ParagraphStyle(
# #         'heading3_arab',
# #         parent = styles['Heading3'],
# #         fontName="Arabic"
        
# #         )

# #     styleBorder = ParagraphStyle(
# #         'border',
# #         parent = styleN ,
# #         borderColor= '#333333',
# #         borderWidth =  1,
# #         borderPadding  =  2,
# #         fontName="Arabic"
# #     )

# #     styleBorderH2 = ParagraphStyle(
# #         'borderH2',
# #         parent = styleH_2 ,
# #         borderColor= '#333333',
# #         borderWidth =  1,
# #         borderPadding  =  2,
# #         fontName="Arabic"
# #     )
# #     story = []

# #     #add the header and the project name
# #     story.append(Paragraph("Business plan",styleH_1))
# #     story.append(Paragraph("This is adraft of a business plan for your idea or project.",styleN))
# #     story.append(Spacer(1,8))
# #     project_name = arabic_reshaper.reshape(list(project.values_list('name', flat=True))[0])
# #     story.append(Paragraph(get_display(project_name),styleBorderH2))
# #     story.append(Spacer(1,8))  


# #     #add the data to pdf
# #     for title, data in zip(titles, all_fields):
        
# #         story.append(Paragraph(title,styleH_3))
# #         story.append(Spacer(1,5))
# #         story.append(Paragraph(str(data),styleBorder))
# #         story.append(Spacer(1,25))

# #     #create the doc
# #     doc = SimpleDocTemplate(buffer, pagesize=letter)
# #     doc.build(story)
# #     pdf = buffer.getvalue()
# #     buffer.close()

# #     return project_name ,pdf