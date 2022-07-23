from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.patientdata.views import save_patient, edit_patient, table_patient


class TestUrls(SimpleTestCase):

    def test_save_url_is_resolved(self):
        url = reverse('patientdata:save_patient')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, save_patient)

    def test_edit_url_is_resolved(self):
        url = reverse('patientdata:edit_patient', kwargs={'id':1})
        # print(resolve(url))
        self.assertEquals(resolve(url).func, edit_patient)

    def test_table_url_is_resolved(self):
        url = reverse('patientdata:table_patient')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, table_patient)
        

