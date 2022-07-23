import django_tables2 as tables
from .models import LabVisit
# from apps.presenthistory.models import PresentHistory
# from apps.pasthistory.models import PastHistory
# from django.core.exceptions import ValidationError

def render_footer(bound_column, table):
    return sum(bound_column.accessor.resolve(row) for row in table.data)
    # s = sum(bound_column.accessor.resolve(row) for row in table.data)
    # return s

class LabVisitTable(tables.Table):
    # def render_id(self, **kwargs):
    #     return kwargs['value'].id

    # def render_forid(self, value, record):
    #     return mark_safe('''<a href=%s>%s</a>''' % (record['id'], value))
        # return "%s" % value

    id = tables.TemplateColumn(
        '<a href="{% url \'labs:edit_lab_visit\' record.id record.patient_id record.visit_id %}">{{ record.id }}</a>',
        verbose_name=u'Lab Visit ID', 
        template_name='django_tables2/bootstrap4.html',
    )
    name = tables.TemplateColumn(
        '<a href="{% url \'labs:edit_lab_visit\' record.id record.patient_id record.visit_id %}">{{ record.name }}</a>',
        verbose_name=u'Analysis Name', 
        template_name='django_tables2/bootstrap4.html',
    )
    result = tables.TemplateColumn(
        '<a href="{% url \'labs:edit_lab_visit\' record.id record.patient_id record.visit_id %}">{{ record.result }}</a>',
        verbose_name=u'Analysis Result', 
        template_name='django_tables2/bootstrap4.html',
    )
    patient = tables.TemplateColumn(
        '<a href="{% url \'labs:edit_lab_visit\' record.id record.patient_id record.visit_id %}">{{ record.patient }}</a>',
        verbose_name=u'Patient Name',
        template_name='django_tables2/bootstrap4.html',
    )

    visit = tables.TemplateColumn(
        '<a href="{% url \'labs:edit_lab_visit\' record.id record.patient_id record.visit_id %}">{{ record.patient }}</a>',
        verbose_name=u'Visit No',
        template_name='django_tables2/bootstrap4.html',
    )

    resdate = tables.TemplateColumn(
        '<a href="{% url \'labs:edit_lab_visit\' record.id record.patient_id record.visit_id %}">{{ record.resdate }}</a>',
        verbose_name=u'Result Date',
    )

    addlab = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'labs:add_lab_visit\' record.patient_id record.id %}">Add Lab Visit</a>',
        verbose_name=u'Add Lab Visit')

    # addpresent = tables.TemplateColumn(
    #     '<a class="btn btn-outline-primary" href="{% url \'presenthistory:save_present_hist\' record.patient_id record.id %}">Add Present History</a>',
    #     verbose_name=u'Add Present History')
    
    deleterec = tables.TemplateColumn(
        '<a class="btn btn-outline-danger" href="{% url \'labs:delete_lab_visit\' record.id record.patient_id record.visit_id %}"'
        'onclick="return confirm(\'Are you sure you want to delete this item ?\')">Delete </a>',
        verbose_name=u'Delete Analysis')

    class Meta:
        model = LabVisit
        attrs = {"id": "labvisit-table",}
        template_name = 'django_tables2/bootstrap4.html'
        fields = ('id', 'name', 'result', 'visit', 'patient', 'resdate',
                  'deleterec', 'addlab')
        # exclude columns while creating the TableExport instance:
        # exporter = TableExport("csv", table, exclude_columns=("image", "buttons"))

