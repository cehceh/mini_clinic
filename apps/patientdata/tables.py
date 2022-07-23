import django_tables2 as tables
from apps.patientdata.models import Patients, Operations
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


class PatientsTable(tables.Table):
    idno = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.id }}</a>',
        verbose_name=u'Patient ID')
    patient = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.name }}</a>',
        verbose_name=u'Patient Name')
    tele = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.phone }}</a>',
        verbose_name=u'Patient Phone')
    mob = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.mobile }}</a>',
        verbose_name=u'Patient Mobile')

    # birth = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.birth_date }}</a>',
    #     verbose_name=u'Birth Date')
    addr = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.address }}</a>',
        verbose_name=u'Address')
    # age = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.age }}</a>',
    #     verbose_name=u'Age')
    crdid = tables.TemplateColumn(
        '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.cardid }}</a>',
        verbose_name=u'Card_ID')
    # followup = tables.TemplateColumn(
    #     '<a class="btn btn-outline-dark" href="{% url \'gyno:add_gyno\' record.id %}">Add Follow Up</a>',
    #     verbose_name=u'Follow Up')
    addvis = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'visits:pass_patient_id\' record.id %}">Add New Visit</a>',
        verbose_name=u'New Visit')
    addpast = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'pasthistory:save_pasthist\' record.id %}">Add Past History</a>',
        verbose_name=u'Past History')
    addop = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'patientdata:save_operation\' record.id %}">Add Operation</a>',
        verbose_name=u'Operation')
    class Meta:
        model = Patients
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "patients-table",
                'class': 'table table-striped table-bordered table-hover'}
        fields = (
            'idno',
            'patient',
            # 'birth',
            # 'age',
            'tele',
            'mob',
            'addr',
            'crdid',
            'addpast',
        )

####################
# def check_column():
#     match_presenthist = PresentHistory.objects.filter(patient={{VisitsTable.record.patient_id}}, visit=VisitsTable.record.id).exists()
#     if match_presenthist:
#         history = tables.TemplateColumn(
#                     '<a class="btn btn-outline-primary" href="/data/present/history/patient/{{record.patient_id}}/visit/{{record.id}}/">Add Present History</a>',
#                     verbose_name=u'Add Present History', visible=False)
#     return history
class OperationsTable(tables.Table):
    idno = tables.TemplateColumn('{{record.id}}',
        verbose_name=u'Operation ID')

    patient = tables.TemplateColumn('{{record.patient}}',
        verbose_name=u'Patient Name')

    # tele = tables.TemplateColumn('{{record.patient.phone}}',
    #     verbose_name=u'Patient Phone')

    mob = tables.TemplateColumn('{{record.patient.mobile}}',
        verbose_name=u'Mobile')

    # birth = tables.TemplateColumn(
    #     '<a href="/clinic/edit/patient/{{record.id}}/">{{ record.birth_date }}</a>',
    #     verbose_name=u'Birth Date')
    # addr = tables.TemplateColumn(
    #     '<a href="{% url \'patientdata:edit_patient\' record.id %}">{{ record.address }}</a>',
    #     verbose_name=u'Address')
    # age = tables.TemplateColumn('{{record.patient.age}}',
    #     verbose_name=u'Age')

    opname = tables.TemplateColumn('{{record.name}}',
        verbose_name=u'Operation Name')

    opdate = tables.TemplateColumn('{{record.opdate}}',
        verbose_name=u'Operation Date')

    editpatient = tables.TemplateColumn(
        '<a class="btn btn-outline-primary" href="{% url \'patientdata:edit_patient\' record.patient_id %}">Edit Patient</a>',
        verbose_name=u'Edit Patient')
    addvis = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'visits:pass_patient_id\' record.patient.id %}">New Visit</a>',
        verbose_name=u'New Visit')
    editop = tables.TemplateColumn(
        '<a class="btn btn-outline-primary" href="{% url \'patientdata:edit_operation\' record.patient.id record.id %}">Edit Operation</a>',
        verbose_name=u'Edit Operation')
    
    addpast = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'pasthistory:save_pasthist\' record.patient.id %}">Add Past History</a>',
        verbose_name=u'Past History')
    addop = tables.TemplateColumn(
        '<a class="btn btn-outline-dark" href="{% url \'patientdata:save_operation\' record.patient.id %}">Add Operation</a>',
        verbose_name=u'Operation')
    class Meta:
        model = Operations
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {"id": "operation-table",
                'class': 'table table-striped table-bordered table-hover'}
        fields = (
            'idno',
            'patient',
            # 'birth',
            # 'age',
            # 'tele',
            'mob',
            # 'addr',
            # 'crdid',
            # 'addpast',
        )
