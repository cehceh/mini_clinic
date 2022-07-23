from django.test import TestCase, Client
from django.urls import reverse
from apps.patientdata.models import Patients, Operations
import json


class TestViews(TestCase):
    #https://stackoverflow.com/questions/60129915/django-tests-matching-query-does-not-exist
    @classmethod          # Making this method to avoid ('Patient matching query doesn't exist')
    def setUpTestData(cls):
        cls.obj_id = Patients.objects.create(name="test_patient").pk

    def setUp(self):
        self.client = Client()
        # self.obj_id = Patients.objects.create(name="testing").pk
        self.save_url = reverse('patientdata:save_patient')
        self.edit_url = reverse('patientdata:edit_patient', kwargs={'id':self.obj_id})
        self.table_url = reverse('patientdata:table_patient')

    def test_save_patient_GET(self):
        response = self.client.get(self.save_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'patientdata/save_patient.html')

    def test_edit_patient_GET(self):
        response = self.client.get(self.edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'patientdata/edit_patient.html')


    def test_table_patient_GET(self):
        response = self.client.get(self.table_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'patientdata/tables.html')

    def test_save_patient_POST(self):
        Patients.objects.create(
            name = "test_patient",
        )

        response = self.client.post(self.edit_url, {
            'id': 1,
        })
        # print('response=:', response)
        patient = Patients.objects.get(id=self.obj_id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(patient.name, 'any')

