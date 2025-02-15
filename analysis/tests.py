from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import AnalysisSheet

class AnalysisSheetTests(TestCase):
    def setUp(self):
        self.analysis_sheet = AnalysisSheet.objects.create(
            id=1,
            sheet_code='test_code',
            sheet_name='Test Sheet'
        )

    def test_analysis_sheet_list_view(self):
        response = self.client.get(reverse('analysis_sheet_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Sheet')

    def test_analysis_sheet_detail_view(self):
        response = self.client.get(reverse('analysis_sheet_detail', args=[self.analysis_sheet.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Sheet')

    def test_analysis_sheet_create_view(self):
        response = self.client.post(reverse('analysis_sheet_create'), {
            'id': 2,
            'sheet_code': 'new_code',
            'sheet_name': 'New Sheet'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(AnalysisSheet.objects.last().sheet_name, 'New Sheet')

    def test_analysis_sheet_update_view(self):
        response = self.client.post(reverse('analysis_sheet_update', args=[self.analysis_sheet.id]), {
            'sheet_code': 'updated_code',
            'sheet_name': 'Updated Sheet'
        })
        self.assertEqual(response.status_code, 302)
        self.analysis_sheet.refresh_from_db()
        self.assertEqual(self.analysis_sheet.sheet_name, 'Updated Sheet')

    def test_analysis_sheet_delete_view(self):
        response = self.client.post(reverse('analysis_sheet_delete', args=[self.analysis_sheet.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(AnalysisSheet.objects.filter(id=self.analysis_sheet.id).exists())