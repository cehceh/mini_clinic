from django import forms
from .models import Revisits
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from django.utils.timezone import now
from datetime import date
# from myproject.tables.table_clinic import MedicineTable

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# from django.contrib.postgres.search import SearchVector

def validate_none(value):
    if value == None:
        raise ValidationError(_('%(value)s must be not NONE'),
            params={'value': '0'},
        )


class RevisitsForm(forms.ModelForm):
    # id = forms.IntegerField(label='Revisit No.',
    #                        widget=forms.NumberInput(
    #                            attrs={
    #                                'class': 'form-control',
    #                                'readonly': 'readonly',
    #                            })
    #                        )

    # visit = forms.ModelChoiceField(queryset=Visits.objects.all(), required=False, label='Visit No',
    #                        widget=forms.Select(
    #                            attrs={
    #                                'class': 'form-control',
    #                                 #    'id': '',
    #                                 # 'disabled':'disabled'
    #                            }))
    # patient = forms.ModelChoiceField(queryset=Patients.objects.all(), required=False, label='Name',
    #                        widget=forms.Select(
    #                            attrs={
    #                                'class': 'form-control',
    #                                 #    'id': '',
    #                                 # 'disabled':'disabled'
    #                            }))

    complain = forms.CharField(required=False, label='Complain',
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                #    'id': '',
                               }))
    sign = forms.CharField(required=False, label='Sign',
                           widget=forms.Textarea(
                               attrs={
                                   'class': 'form-control',
                                #    'id': '',

                               }))
    visitdate = forms.DateField(required=True, label='Revisit Date',
                           widget=forms.TextInput(
                               attrs={
                                    'class': 'form-control',
                                    # 'placeholder':'Click here to enter the visit date ...',
                                    'value': date.today(),
                                    'id': 'visitdate',
                                    'type':'date',
                                    # 'readonly': 'readonly'
                               }
                           ))
    diagnosis = forms.CharField(required=False, label='Daignosis',
                            widget=forms.TextInput(
                                attrs={
                                   'class': 'form-control',
                                #    'id': '',

                               })
                            )
    intervention = forms.CharField(required=False, label='Intervention',
                            widget=forms.TextInput(
                                attrs={
                                   'class': 'form-control',
                                #    'id': '',

                               })
                            )
    amount = forms.IntegerField(required=True, label='Amount', #validators=[validate_none],
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'form-control',
                                #    'id': '',
                                    'value':'0'
                               }
                           ))
    def clean(self): # this method for prevent save or update the field 'amount' if it is None
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        visitdate = cleaned_data.get('visitdate')
        if amount == None:
            self.add_error('amount', 'can not be empty') # the error as outline (red line) of the input
            raise ValidationError('Amount Can Not Be Empty')
        # if visitdate == None:
        #     self.add_error('visitdate', 'Date can\'t be Empty')
        #     raise ValidationError('Revisit Date Can Not Be Empty')
            # return msg
        return cleaned_data

    class Meta:
        model = Revisits
        fields = ('__all__')