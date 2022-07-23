import django_tables2 as tables
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.visitdrug.models import Medicine
from .models import Revisits
# from patientdata.models import PresentHistory
# from django.core.exceptions import ValidationError


def render_footer(bound_column, table):
    # for row in table.data:
    #     s = sum(bound_column.accessor.resolve(row))
    return sum(bound_column.accessor.resolve(row) for row in table.data)
    # s = sum(bound_column.accessor.resolve(row) for row in table.data)
    # return s

def countrow(table):
    return len(table.rows)


class RevisitsTable(tables.Table):
    # patid = Patients.objects.get(id=)
    # path = '<a href="{% url \'revisits:edit_revisit\' record.patient_id record.visit record.id %}">{{ record.id }}</a>'
    # def render_rec(self, record):
    #     return "{}".format(record.patient_id)
        # return mark_safe(''' <a href="{% url \'revisits:edit_revisit\' record.patient_id record.visit record.id %}">%s</a> ''' % (record.patient, value))

    id = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.id}}</a>',
        verbose_name=u'Revisit ID',)
    visit = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.visit}}</a>',
        verbose_name=u'Visit No',)
    patient = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.patient}}</a>',
        verbose_name=u'Patient Name',)

    revisitdate = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.visitdate}}</a>',
        verbose_name=u'Revisit Date',
    )

    diagnosis = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.diagnosis}}</a>',
        verbose_name=u'Revisit Daignosis',  #footer=len(tables.rows)
    )
    
    amount = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.amount}}</a>',
        verbose_name=u'Revisit Amount', footer=render_footer)

    visitdate = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.visit.visitdate}}</a>',
        verbose_name=u'Visit Date',
    )

    visitdia = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.visit.diagnosis}}</a>',
        verbose_name=u'Visit Daignosis',  #footer=len(tables.rows)
    )
    
    visamount = tables.TemplateColumn(
        '<a href="{% url \'revisits:edit_revisit\' record.id record.patient_id record.visit %}">{{record.visit.amount}}</a>',
        accessor='visit.amount',
        verbose_name=u'Visit Amount', footer=render_footer)

    prn = tables.TemplateColumn(
        '<a class="btn btn-outline-secondary" href="#under_construction">Add Prescription</a>',
        verbose_name=u'Add Prescription')

    addrevis = tables.TemplateColumn(
        '<a class="btn btn-outline-primary" href="{% url \'revisits:save_revisit\' record.patient_id record.visit %}">Add Revisit</a>',
        verbose_name=u'Add Revisit')

    editvis = tables.TemplateColumn(
        '<a class="btn btn-outline-primary" href="{% url \'visits:visits_patient_id\' record.visit record.patient_id %}">Update Visit</a>',
        verbose_name=u'Update Visit')
    
    delrevis = tables.TemplateColumn(
        '<a class="btn btn-outline-danger" href="{% url \'revisits:delete_revisit\' record.id %}" '
        'onclick="return confirm(\'Are you sure you want to delete this Revisit ?\')">Delete Revisit</a>',
        verbose_name=u'Delete Revisit')

    class Meta:
        model = Revisits
        attrs = {"id": "revisits-table"}
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'visit', 'patient', 'revisitdate', 'diagnosis', 'amount', 'visitdate', 'visitdia', 'visamount',  
                  'prn', 'addrevis', 'editvis', 'delrevis',)
        # exclude columns while creating the TableExport instance:
        # exporter = TableExport("csv", table, exclude_columns=("image", "buttons"))





