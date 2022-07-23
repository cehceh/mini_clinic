from django import forms
# from django.forms import ModelForm
from .models import Medicine
from django.utils.timezone import now
from datetime import date
from .tables import MedicineTable
from apps.patientdata.models import Patients
from apps.visits.models import Visits


from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MedicineForm(forms.ModelForm):
    # patient = forms.ModelChoiceField(queryset=Patients.objects.all(), required=True, label='Patient Name',
    #                        widget=forms.Select(
    #                            attrs={
    #                                'class': 'form-control',
    #                                'id': 'patient',
    #                             #    'v-model': "patient_name",
    #                                 # 'disabled':'disabled'
    #                            }))
    
    # visit = forms.ModelChoiceField(queryset=Visits.objects.all(), required=True, label='Visit No.',
    #                        widget=forms.Select(
    #                            attrs={
    #                                'class': 'form-control',
    #                                'id': 'visit-id',
    #                                 # 'readonly':'readonly'
    #                            }))

    name = forms.CharField(error_messages={'required':"Please fill this field ..."}, label='Drug',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'id': 'name',
                                    #    'lang': 'arabic',
                                        'placeholder':'Type Your Drug ...',
                                   }))

    plan = forms.CharField(required=False, label='Plan',
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control',
                                       'id': 'plan',
                                       'lang': 'arabisk',
                                        'placeholder':'Type Your Plan ...',
                                   }))

    # presc = forms.CharField(required=False,
    #                        label='Pre ID',
    #                        widget=forms.TextInput(
    #                            attrs={
    #                                'class': 'form-control',
    #                             #    'id': '',
    #                             #    'lang': 'arabisk',
    #                             #    'placeholder': 'Type Your Plan ...',
    #                             # 'readonly':
    #                            }))
    
    class Meta:
        model = Medicine
        fields = ('name', 'plan')#('__all__')
        # fields = ('__str__', 'address', )

    # init function is importanat in saving user automatically in create() function
    def __init__(self, *args, **kwargs):
        # self.user = user
        super(MedicineForm, self).__init__(*args, **kwargs)
    # def clean(self):
    #     cleaned = super().clean()
    #     visit_id = cleaned.get('visit')
    #     table = MedicineTable(Medicine.objects.filter(visit=visit_id))
    #     # row_count = self.countrow(MedicineTable)
    #     row_count = len(table.rows)
    #     if row_count > 2:
    #         raise ValidationError('Drugs must be 2 or less')

    # these three lines make the error appears in the templates
    # <div style="background-color: pink;">
    #         {{save_visits_form.non_field_errors}}
    #     </div>
    # return cleaned_data
