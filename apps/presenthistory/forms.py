from django import forms
# from django.forms import ModelForm
from apps.patientdata.models import Patients
from apps.visits.models import Visits
from apps.presenthistory.models import PresentHistory
from datetime import date

# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
# from django.contrib.postgres.search import SearchVector

# def validate_none(value):
#     if value == None:
#         raise ValidationError(
#             _('%(value)s must be not NONE'),
#             params={'value': '0'},
#         )
class PresentHistoryForm(forms.ModelForm):
    # id = forms.IntegerField(
    #     required=False,
    #     label='ID',
    #     widget=forms.NumberInput(attrs={
    #         'class': 'form-control',
    #         'readonly': 'readonly',
    #     }))

    # visitdate = forms.DateField(
    #     required=True,
    #     label='Visit Date',
    #     widget=forms.TextInput(attrs={
    #             'class': 'form-control',
    #             'id': 'visitdate',
    #             'type': 'text',
    #             # 'name': '',
    #             # 'placeholder': date.today(),
    #             'readonly': 'readonly', # to make an input disabled
    #         }))

    # patient = forms.ModelChoiceField(
    #     queryset=Patients.objects.all(),
    #     required=True,
    #     label='Patient Name',
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'patient',
    #             # 'disabled':'disabled',
    #             'readonly': 'readonly',
    #         }))

    # visit = forms.ModelChoiceField(
    #     queryset=Visits.objects.all(),
    #     required=True,
    #     label='Visit No.',
    #     widget=forms.Select(attrs={
    #         'class': 'form-control',
    #         'id': 'visit-id',
    #         'readonly':'readonly'
    #     }))

    temprature = forms.CharField(
        required=False, empty_value='0.00',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            # 'id': '',
            'value':'00.00',
        }))

    weight = forms.DecimalField(
        required=False, 
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                'value':'000.00'
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    height = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                'value':'000.00'
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    cholestrol = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    pulse = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    bloodpr = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    bsl = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    hb = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                # 'id': 'age',
                'type': 'text',
                # 'name': 'age',
                # 'readonly': 'readonly', # to make an input disabled
            }))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     cardid = cleaned_data.get('cardid')
    #     match = Patients.objects.filter(cardid=cardid).exists()
    #     if match == True or cardid == None:
    #         self.add_error('cardid', 'Card ID must not be Empty or Repeated'
    #                        )  # the error as outline (red line) of the input
    #         raise ValidationError(
    #             'Card ID must not be Empty or Repeated valid error')
    #     return cleaned_data

    class Meta:
        model = PresentHistory
        fields = ('temprature', 'weight', 'height', 
                'cholestrol', 'bloodpr', 'hb', 'pulse', 'bsl') #('__all__')
        # exclude = ['patient', 'visitdate', 'visit']
