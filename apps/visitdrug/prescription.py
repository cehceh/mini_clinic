from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect

# from django.views.generic import View
# from django.template.loader import get_template
# from clinic.utils import render_to_pdf # Justin code
import time
from django.contrib import messages

from .models import Medicine, Patients, Visits
from .forms import MedicineForm
from apps.patientdata.forms import PatientsForm
from apps.visits.forms import VisitsForm
from .tables import MedicineTable


# This method to print prescription
def print_html(request, visit_id):
    vis_id = Visits.objects.get(id=visit_id)
    table = MedicineTable(Medicine.objects.filter(visit=visit_id).order_by('-id'), show_header=False)
    qs = Medicine.objects.filter(visit=visit_id).order_by('-id') 

    patname = Medicine.objects.values('patient').filter(visit=visit_id).first()
    patid = Medicine.objects.values('patient_id').filter(visit=visit_id).first()
    # pat_id = patid['patient_id']
    print(patid)
    match = Medicine.objects.filter(visit=visit_id).exists()
    if match:
        patient = Patients.objects.get(id=patname['patient'])#patname['patient']
    else:
        patient = None
        messages.success(request, 'Prescription is not ready create new one')
    
    vdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
    visitdate = vdate['visitdate']

    context = {
        'match_patient': match,
        'raw_table': table,
        'qs': qs,
        'visit_no': vis_id,
        'name': patient,
        'date': visitdate,
    }
    return render(request, 'visitdrug/print.html', context)


# # This is func based to render to pdf
# def get_pdf(request, visit_id, *args, **kwargs):
#     vis_id = Visits.objects.get(id=visit_id)
#     qs = Medicine.objects.filter(visit=visit_id).order_by('-id')
#     plan = Medicine.objects.values('plan').filter(visit=visit_id).first()
#     plan1 = Medicine.objects.filter(plan=plan['plan'])
#     vdate = Visits.objects.values('visitdate').filter(id=visit_id).first()
#     visitdate = vdate['visitdate']

#     patname = Medicine.objects.values('patient').filter(visit=visit_id).first()
#     patient = Patients.objects.get(id=patname['patient'])#patname['patient']

#     print(patient , plan1)
#     # plan = qs1['plan']
#     # for obj in plan:
#         # print(obj['plan'])
#         # p = obj['plan'] #araby.tokenize()
#         # return p   

#     query = Medicine.objects.all().order_by('-id')
#     # print()
#     # zero_remain = LaundryBill.objects.filter(sumtotal__gt=0, returns=False, remain=0).order_by('-id')
#     template = get_template('clinic/pdf.html')
#     context = { 
#         # 'p': p,
#         'qs': qs,
#         "query":query,
#         "visit_no": vis_id,
#         "name": patient,
#         "date": visitdate,
#         "today": "Today",
#     }
#     html = template.render(context)
#     pdf = render_to_pdf('clinic/pdf.html', context)
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


# def pdf_view(request, *args, **kwargs):
#     # with open('/path/to/my/file.pdf', 'r') as pdf:
#     #     response = HttpResponse(pdf.read(), ContentType='application/pdf')
#     #     response['Content-Disposition'] = 'inline;filename=some_file.pdf'
#     #     return response
#     # pdf.closed
#     objkey = kwargs.get('pk', None) #1
#     pdf = get_object_or_404(Pdf, pk=objkey) #2
#     fname = pdf.filename() #3
#     path = os.path.join(settings.MEDIA_ROOT, 'docs\\' + fname)#4
#     response = FileResponse(open(path, 'rb'), content_type="application/pdf")
#     response["Content-Disposition"] = "filename={}".format(fname)
#     return response

# import io
# from django.http import FileResponse
# # from reportlab.pdfgen import canvas

# # def some_view(request):
# #     # Create a file-like buffer to receive PDF data.
# #     buffer = io.BytesIO()

# #     # Create the PDF object, using the buffer as its "file."
# #     p = canvas.Canvas(buffer)

# #     # Draw things on the PDF. Here's where the PDF generation happens.
# #     # See the ReportLab documentation for the full list of functionality.
# #     p.drawString(100, 100, "Hello world.")

# #     # Close the PDF object cleanly, and we're done.
# #     p.showPage()
# #     p.save()

# #     # FileResponse sets the Content-Disposition header so that browsers
# #     # present the option to save the file.
# #     buffer.seek(0)
# #     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


# # from django.core.files.storage import FileSystemStorage
# # from django.http import HttpResponse
# # from django.template.loader import render_to_string

# # from weasyprint import HTML

# # def html_to_pdf_view(request):
# #     paragraphs = ['first paragraph', 'بسم الله', 'third paragraph']
# #     html_string = render_to_string('clinic/pdf.html', {'paragraphs': paragraphs})

# #     html = HTML(string=html_string)
# #     html.write_pdf(target='/tmp/mypdf.pdf');

# #     fs = FileSystemStorage('/tmp')
# #     with fs.open('mypdf.pdf') as pdf:
# #         response = HttpResponse(pdf, content_type='application/pdf')
# #         response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
# #         return response

# #     return response