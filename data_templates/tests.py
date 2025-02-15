from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import DataTemplate

class DataTemplateTests(TestCase):
    def setUp(self):
        self.data_template = DataTemplate.objects.create(
            name='Test Template',
            description='Test Description',
            category_id=1,
            used_n=0
        )

    def test_list_data_templates(self):
        response = self.client.get(reverse('data_template_list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_data_template(self):
        response = self.client.get(reverse('data_template_detail', args=[self.data_template.id]))
        self.assertEqual(response.status_code, 200)

    def test_create_data_template(self):
        response = self.client.post(reverse('data_template_create'), {
            'name': 'New Template',
            'description': 'New Description',
            'category_id': 2,
            'used_n': 1
        })
        self.assertEqual(response.status_code, 201)

    def test_update_data_template(self):
        response = self.client.post(reverse('data_template_update', args=[self.data_template.id]), {
            'name': 'Updated Template',
            'description': 'Updated Description',
            'category_id': 1,
            'used_n': 1
        })
        self.assertEqual(response.status_code, 200)

    def test_delete_data_template(self):
        response = self.client.post(reverse('data_template_delete', args=[self.data_template.id]))
        self.assertEqual(response.status_code, 204)