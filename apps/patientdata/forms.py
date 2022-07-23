from django import forms
# from django.forms import ModelForm, fields
from .models import Patients, Operations
# from django.utils.timezone import now
from datetime import date
# from apps.visitdrug.tables import MedicineTable
# from apps.visitdrug.models import Medicine
# from apps.visits.models import Visits

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# from django.contrib.postgres.search import SearchVector

def validate_none(value):
    if value == None:
        raise ValidationError(_('%(value)s must be not NONE'),
            params={'value': '0'},
        )

        
# you will write your class forms to be appear to the users
class PatientsForm(forms.ModelForm):
    id = forms.IntegerField(required=False, label='Patient ID',
                           widget=forms.NumberInput(
                               attrs={
                                   'class': 'form-control',
                                   'readonly': 'readonly',
                               })
                           )
    name = forms.CharField(required=True,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'name',
                }
            ))
    address = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'address',
                }
            ))
    birth_date = forms.DateField(required=True,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'birth-date',
                    'type': 'date',
                    'name': 'dob',
                    'value':date.today(),
                    # 'placeholder': date.today(),
                    # 'readonly': 'readonly', # to make an input disabled
                })
            )
    cardid = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'cardid',
                    # 'type': 'number',
                }
            ))
    phone = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'phone',
                }
            ))
    mobile = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id': 'mobile',
                }
            ))
    
    age = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'age',
                    'type': 'text',
                    # 'name': 'age',
                    'readonly': 'readonly', # to make an input disabled
                }
            ))
    job = forms.CharField(required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'age',
                    'type': 'text',
                    # 'name': 'age',
                    # 'readonly': 'readonly', # to make an input disabled
                }
            ))
    
    # barcode = forms.CharField(required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 'class':'form-control',
    #                 # 'id': 'age',
    #                 'type': 'text',
    #                 # 'name': 'age',
    #                 'readonly': 'readonly', # to make an input disabled
    #             }
    #         ))

    # barurl = forms.CharField(required=True,
    #         widget=forms.TextInput(
    #             attrs={
    #                 'class':'form-control',
    #                 # 'id': 'age',
    #                 'type': 'text',
    #                 # 'name': 'age',
    #                 'readonly': 'readonly', # to make an input disabled
    #             }
    #         ))


    class Meta:
        model = Patients
        fields = '__all__'
        # fields = ('__str__', 'address', )

    # def __init__(self, *args, **kwargs):
    #     # self.user = user
    #     super(PatientsForm, self).__init__(*args, **kwargs)
    # def clean_name(self):
    #     cleaned_data = super().clean()
    #     # patid = cleaned_data.get('id')
    #     # print(patid)
    #     # match_id = Patients.objects.filter(id=Patients.id).exists()
    #     name = cleaned_data.get('name')
    #     match_name = Patients.objects.filter(name=name).exists()
    #     if match_id == False:
    #         if match_name:
    #         # self.add_error('name', 'Patient name must be unique') # the error as outline (red line) of the input
    #         # self.add_error('cardid', 'Card ID must not be Empty or Repeated') # the error as outline (red line) of the input
    #             raise ValidationError('Patient name must be unique')
    #     # else:
    #     #     raise ValidationError('Card ID must not be Empty or Repeated')
    #     return cleaned_data

# barimg = forms.ImageField(required=False,
    #         widget=forms.ClearableFileInput(
    #             # attrs={
    #             #     'class':'form-control',
    #             #     # 'id': 'age',
    #             #     # 'type': 'text',
    #             #     # 'name': 'age',
    #             #     # 'readonly': 'readonly', # to make an input disabled
    #             # }
    #         ))

class OperationsForm(forms.ModelForm):
    
    name = forms.CharField(required=True, label= "Operation Name", 
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'age',
                    'type': 'text',
                    # 'name': 'age',
                    # 'readonly': 'readonly', # to make an input disabled
                }
            ))
    opdate = forms.DateField(label= "Operation Date",
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'age',
                    'type': 'date',
                    'value': date.today(),
                    # 'readonly': 'readonly', # to make an input disabled
                }
            ))
    # amount = forms.CharField(label= "Amount", required=False,
    #         widget=forms.TextInput(
    #             attrs={
    #                 'class':'form-control',
    #                 # 'id': 'age',
    #                 'type': 'number',
    #             }
    #         ))
    followup = forms.CharField(label="Follow Up", required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'age',
                    'type': 'text',
                    # 'name': 'age',
                    # 'readonly': 'readonly', # to make an input disabled
                }
            ))
    improve = forms.CharField(label="Improvement", required=False,
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    # 'id': 'age',
                    'type': 'text',
                    # 'name': 'age',
                    # 'readonly': 'readonly', # to make an input disabled
                }
            ))
    remark = forms.CharField(label="Description", required=False,
            widget=forms.Textarea(
                attrs={
                    'class':'form-control',
                    'type': 'text',
                }
            ))

    class Meta:
        model = Operations
        fields = ('name', 'opdate', 'followup', 'improve', 'heal', 'remark', 'amount')#'__all__'
    
    # def __init__(self, *args, **kwargs):
    #     super(OperationsForm, self).__init__(*args, **kwargs)
