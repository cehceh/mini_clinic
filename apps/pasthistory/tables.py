import django_tables2 as tables
# from clinic.models import Patients, Visits, Medicine
from .models import PastHistory
from django.core.exceptions import ValidationError


def render_footer(bound_column, table):
    return sum(bound_column.accessor.resolve(row) for row in table.data)
    # s = sum(bound_column.accessor.resolve(row) for row in table.data)
    # return s

def countrow(table):
    return len(table.rows)



class PastHistoryTable(tables.Table):
    patient = tables.TemplateColumn(
        '<a href="{% url \'pasthistory:edit_pasthist\' record.patient_id record.id %}">{{ record.patient }}</a>',
        # accessor='patient.pasthist',
        verbose_name=u'Patient Name')
    pasthist = tables.TemplateColumn(
        '<a href="{% url \'pasthistory:edit_pasthist\' record.patient_id record.id %}">{{ record.pasthist }}</a>',
        # accessor='patient.pasthist',
        verbose_name=u'Past History')
    histdate = tables.TemplateColumn(
        '<a href="{% url \'pasthistory:edit_pasthist\' record.patient_id record.id %}">{{ record.histdate }}</a>',
        verbose_name=u'History Date')
    add = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'pasthistory:edit_pasthist\' record.patient_id record.id %}">Add Past History</a>',
        verbose_name=u'Add Past History')
    delete = tables.TemplateColumn(
        '<a class="btn btn-outline-danger" href="{% url \'pasthistory:delete_pasthist\' record.id %}"'
        'onclick="return confirm(\'Are you sure you want to delete this item ?\')">Delete Record</a>',
        verbose_name=u'Delete Past History')
    class Meta:
        model = PastHistory
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "past-history-table"}
        fields = (
            # 'idno',
            'patient',
            'histdate',
            # 'remark',
            'pasthist',
            'add',
            'delete',
        )

