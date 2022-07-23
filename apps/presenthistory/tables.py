import django_tables2 as tables
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.visitdrug.models import Medicine
from apps.presenthistory.models import PresentHistory
from apps.pasthistory.models import PastHistory
# from django.core.exceptions import ValidationError


def render_footer(bound_column, table):
    return sum(bound_column.accessor.resolve(row) for row in table.data)
    # s = sum(bound_column.accessor.resolve(row) for row in table.data)
    # return s

def countrow(table):
    return len(table.rows)

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


class PresentHistoryTable(tables.Table):
    # idno = tables.TemplateColumn(
    #     template_code='<a href="/clinic/edit/patient/{{record.id}}/">{{ record.id }}</a>',
    #     accessor='id',
    #     verbose_name=u'ID')
    visno = tables.Column(accessor='visit',
        # '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.visit }}</a>',
        verbose_name=u'Visit ID')
    patient = tables.Column(accessor='patient',
        # '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.patient }}</a>',
        verbose_name=u'Patient Name')
    visdate = tables.Column(
        # '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.visit.visitdate }}</a>',
        accessor='visit.visitdate',
        verbose_name=u'Visit Date')

    dia = tables.Column(
        # template_code='<a href="/clinic/edit/patient/{{record.id}}/">{{record.visit.diagnosis}}</a>',
        accessor='visit.diagnosis',
        verbose_name=u'Daignosis')

    # birth = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.birth_date }}</a>',
    #     verbose_name=u'Birth Date')
    # addr = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.address }}</a>',
    #     verbose_name=u'Address')
    # age = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.age }}</a>',
    #     verbose_name=u'Age')
    cardid = tables.Column(
        # '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.patient.cardid }}</a>',
        accessor='patient.cardid',
        verbose_name=u'Card ID')
    edit = tables.TemplateColumn(
        '<a class="btn btn-outline-primary" href="{% url \'presenthistory:edit_present_hist\' record.patient_id record.visit record.id %}">Update Present History</a>',
        verbose_name=u'Update Present History')
    delete = tables.TemplateColumn(
        '<a class="btn btn-outline-danger" href="{% url \'presenthistory:delete_history\' record.id %}"'
        'onclick="return confirm(\'Are you sure you want to delete this item ?\')">Delete Present History</a>',
        verbose_name=u'Detete Present History')

    class Meta:
        model = PresentHistory
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "present-history-table",
                'class': 'table table-striped table-bordered table-hover'}
        fields = (
            # 'idno',
            'visno',
            'patient',
            'visdate',
            'dia',
            'cardid',
            'edit',
            'delete',
        )



