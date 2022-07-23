from django import forms
# from django.forms import ModelForm
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.pasthistory.models import PastHistory
# from django.utils.timezone import now
from datetime import date

# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# from django.contrib.postgres.search import SearchVector


class PastHistoryForm(forms.ModelForm):
    histdate = forms.DateField(
        required=True,
        label='History Date',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'histdate',
                'type': 'date',
                'value': date.today(),
            }))
    pasthist = forms.CharField(
        required=True, 
        label='Past History',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'pasthist',
            'type': 'text',
            'placeholder':'write the past history for your patient',
        }))

    remarknote = forms.CharField(
        required=False, 
        label='Remarks',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'type': 'text',
            'placeholder':'write notes about past history for your patient',
            'value':'',
        }))

    patient = forms.ModelChoiceField(
                    queryset=Patients.objects.all(),
                    required=False,
                    label='Patient Name',
                    widget=forms.Select(
                        attrs={
                            'class': 'form-control',
                            'id': 'patient',
                            'readonly': 'readonly',
                        }))
    # def clean(self):
    #     cleaned_data = super().clean()
    #     patient = cleaned_data.get('patient')
    #     match_patient = PastHistory.objects.filter().exists()
    class Meta:
        model = PastHistory
        fields = ('histdate', 'pasthist', 'remarknote', 'patient')#('__all__')


    # def __init__(self, *args, **kwargs):
    #     super(PastHistoryForm, self).__init__(*args, **kwargs)
    #     self.fields['pasthist'].widget.attrs['class'] = 'form-control'
    #     self.fields['histdate'].widget.attrs['class'] = 'form-control'
    #     self.fields['remark'].widget.attrs['class'] = 'form-control'
        # self.fields['patient'].widget.attrs['class'] = 'form-control'
        # self.fields['patient'].queryset[] = (Patients.objects.all())
