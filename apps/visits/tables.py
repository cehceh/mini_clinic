import django_tables2 as tables
from .models import Visits
from apps.presenthistory.models import PresentHistory
from apps.pasthistory.models import PastHistory
# from django.core.exceptions import ValidationError
from django.db.models import Sum
import itertools
# class AmountColumn(tables.Column):
#     column_total = 0

#     def render(self, record):
#         total = record.amount.aggregate(total=Sum("amount"))['total']
#         self.column_total += total
#         return total

#     def render_footer(self, bound_column, table):
#         return sum(bound_column.accessor.resolve(row) for row in table.data)
        # return round(self.column_total, 2)

# class BillsColumn(tables.Column):
#     column_total = 0
#     def render(self, record):
#         bills = record.certificatebills.all()
#         total_bill = 0
#         for bill in bills:
#             total_bill += bill.bill_amount
#         # accumulate
#         self.column_total += total_bill
#         return round(total_bill, 2)

#     def render_footer(self, bound_column, table):
#         return sum(bound_column.accessor.resolve(row) for row in table.data)



# def render_footer(self, bound_column, table):
#     return round(self.column_total, 2)
def render_footer(bound_column, table):
    return sum(bound_column.accessor.resolve(row) for row in table.data)

# def render_footer(bound_column, page):
#     return sum(bound_column.accessor.resolve(row) for row in page.data)
# def amount_footer(table):
#     return sum(x['sum_amount'] for x in table.data)
# def render_amount():
#     row_amount = getattr('amount', itertools.count())
#     return next(row_amount)

class VisitsTable(tables.Table):
    # def render_footer(self, bound_column, table):
    #     return sum(self.bound_column.accessor.resolve(row) for row in table.data)
        # return round(self.column_total, 2)
    amount = tables.TemplateColumn(
        '<a href="{% url \'visits:visits_patient_id\' record.id record.patient_id %}">{{ record.amount }}</a>',
        verbose_name=u'Amount',
        footer="")
    

    id = tables.TemplateColumn(
        '<a href="{% url \'visits:visits_patient_id\' record.id record.patient_id %}">{{ record.id }}</a>',
        verbose_name=u'Visits ID', 
        template_name='django_tables2/bootstrap4.html',
    )
    patient = tables.TemplateColumn(
        '<a href="{% url \'visits:visits_patient_id\' record.id record.patient_id %}">{{ record.patient }}</a>',
        verbose_name=u'Patient Name',
        template_name='django_tables2/bootstrap4.html',
    )

    visitdate = tables.TemplateColumn(
        '<a href="{% url \'visits:visits_patient_id\' record.id record.patient_id %}">{{ record.visitdate }}</a>',
        verbose_name=u'Visit Date',
    )

    diagnosis = tables.TemplateColumn(
        '<a href="{% url \'visits:visits_patient_id\' record.id record.patient_id %}">{{ record.diagnosis }}</a>',
        verbose_name=u'Daignosis',  #footer=len(tables.rows)
    )
    # amount = tables.TemplateColumn(
    #     '<a href="{% url \'visits:visits_patient_id\' record.id record.patient_id %}">{{ record.amount }}</a>',
    #     verbose_name=u'Amount',
    #     footer=render_footer)

    addlab = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'labs:add_lab_visit\' record.patient_id record.id %}">Add Analysis</a>',
        verbose_name=u'Add Analysis',
        footer="")

    addpresent = tables.TemplateColumn(
        '{% if record.id in var %}'
        '<a class="btn btn-outline-secondary" href="{% url \'presenthistory:save_present_hist\' record.patient_id record.id %}">Show Present History</a>'
        '{% else %}'
        '<a class="btn btn-outline-danger" href="{% url \'presenthistory:save_present_hist\' record.patient_id record.id %}">Add Present History</a>'
        '{% endif %}',
        verbose_name=u'Add Present History')
    
    # addrevis = tables.TemplateColumn(
    #     '<a class="btn btn-outline-dark" href="{% url \'revisits:save_revisit\' record.patient_id record.id %}">Add Revisit</a>',
    #     verbose_name=u'Add Revisit')

    class Meta:
        model = Visits
        # attrs = {"id": "visits-table",}
        attrs = {"id": "visits-table",
                'class': 'table table-striped table-bordered table-hover'}
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'patient', 'visitdate', 'diagnosis', 'amount',
                'addlab')
        # exclude columns while creating the TableExport instance:
        # exporter = TableExport("csv", table, exclude_columns=("image", "buttons"))

